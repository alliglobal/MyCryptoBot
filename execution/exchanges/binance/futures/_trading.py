import logging

import pytz
import os
from datetime import datetime

import django
from binance.exceptions import BinanceAPIException

from execution.exchanges.binance import BinanceTrader
from shared.exchanges import BinanceHandler
from shared.trading import Trader
from execution.exchanges.binance.helpers import binance_error_handler
from shared.utils.decorators.failed_connection import retry_failed_connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")
django.setup()

from database.model.models import Symbol


class BinanceFuturesTrader(BinanceTrader):

    def __init__(
        self,
        paper_trading=False
    ):
        BinanceHandler.__init__(self, paper_trading)
        Trader.__init__(self, 0)

        self.paper_trading = paper_trading
        self.max_borrow_amount = {}
        self.symbols = {}
        self.positions = {}
        self.equity = {}
        self.initial_balance = {}
        self.current_balance = {}
        self.units = {}

        self.open_orders = []
        self.filled_orders = []
        self.conn_key = None
        self.exchange = "binance"

    # TODO: Make equity mandatory
    def start_symbol_trading(self, symbol, equity=0, leverage=None, header='', **kwargs):

        if symbol in self.symbols:
            return True

        self.equity[symbol] = equity

        if isinstance(leverage, int):
            try:
                self.futures_change_leverage(symbol=symbol, leverage=leverage)
            except BinanceAPIException as e:
                logging.info(e)

        # TODO: Make call to API to check against existing accounts'
        try:
            symbol_obj = Symbol.objects.get(name=symbol)
            self.symbols[symbol] = {"base": symbol_obj.base.symbol, "quote": symbol_obj.quote.symbol}
        except Symbol.DoesNotExist:
            return False

        self._set_initial_position(symbol, header)

        self._set_initial_balance(symbol, equity, header=header)

        return True

    def stop_symbol_trading(self, symbol, header='', **kwargs):

        if symbol not in self.symbols:
            return False

        logging.info(header + f"Closing position for symbol: {symbol}")

        position_closed = self.close_pos(symbol, date=datetime.now(tz=pytz.UTC), header=header, **kwargs)

        self.symbols.pop(symbol)

        return position_closed

    def close_pos(self, symbol, date=None, row=None, header='', **kwargs):

        if self.units[symbol] == 0:
            return False

        if self.units[symbol] < 0:
            self.buy_instrument(symbol, date, row, units=-3*self.units[symbol], header=header, reduceOnly=True, **kwargs)
        else:
            self.sell_instrument(symbol, date, row, units=3*self.units[symbol], header=header, reduceOnly=True, **kwargs)

        self._set_position(symbol, 0, previous_position=1, **kwargs)

        self.print_trading_results(header, date, symbol=symbol)

        return True

    @retry_failed_connection(num_times=2)
    @binance_error_handler
    def _execute_order(
        self,
        symbol,
        order_type,
        order_side,
        going,
        units,
        amount=None,
        header='',
        **kwargs
    ):

        if amount is not None and units is None:
            units = self._convert_amount_to_units(amount, symbol)

        pipeline_id = kwargs["pipeline_id"] if "pipeline_id" in kwargs else None

        order = self.futures_create_order(
            symbol=symbol,
            side=order_side,
            type=order_type,
            newOrderRespType='RESULT',
            quantity=units,
            **kwargs
        )

        order["price"] = order["avgPrice"]

        order = self._process_order(order, pipeline_id)

        factor = 1 if order_side == self.SIDE_SELL else -1

        units = float(order["executed_qty"])

        self.current_balance[symbol] += factor * float(order['cummulative_quote_qty'])
        self.units[symbol] -= factor * units

        self.trades += 1

        self.report_trade(order, units, going, header, symbol=symbol)

    def _convert_amount_to_units(self, amount, symbol):
        price = float(self.get_symbol_ticker(symbol=symbol)['price'])
        return round(amount / price, 5)

    def _format_order(self, order, pipeline_id):
        return dict(
            order_id=order["orderId"],
            client_order_id=order["clientOrderId"],
            symbol_id=order["symbol"],
            transact_time=datetime.fromtimestamp(order["updateTime"] / 1000).astimezone(pytz.utc),
            price=float(order["avgPrice"]),
            original_qty=float(order["origQty"]),
            executed_qty=float(order["executedQty"]),
            cummulative_quote_qty=float(order["cumQty"]),
            status=order["status"],
            type=order["type"],
            side=order["side"],
            mock=self.paper_trading,
            pipeline_id=pipeline_id
        )

    # TODO: Add last order position
    def _set_initial_balance(self, symbol, amount, factor=1, header=''):
        logging.debug(header + f"Updating balance for symbol: {symbol}.")

        balance = amount * factor

        self.units[symbol] = 0
        self.current_balance[symbol] = balance
        self.initial_balance[symbol] = balance