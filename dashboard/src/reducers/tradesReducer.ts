import {Trade} from "../types";

export const UPDATE_TRADES_STATISTICS = 'UPDATE_TRADES_STATISTICS'

export const tradesReducerCallback = (metrics: any, trade: Trade) => {
  return {
    numberTrades: metrics.numberTrades + 1,
    maxTradeDuration: trade.openTime < metrics.maxTradeDuration ? trade.openTime : metrics.maxTradeDuration,
    totalTradeDuration: trade.closeTime ? trade.closeTime.getTime() - trade.openTime.getTime()
      : new Date().getTime() - trade.openTime.getTime(),
    winningTrades: trade.profitLoss && trade.profitLoss > 0 ? metrics.winningTrades + 1 : metrics.winningTrades,
    closedTrades: trade.profitLoss ? metrics.closedTrades + 1 : metrics.closedTrades,
    bestTrade: metrics.bestTrade ? trade.profitLoss && trade.profitLoss > metrics.bestTrade
      ? trade.profitLoss : metrics.bestTrade : trade.profitLoss,
    worstTrade: metrics.worstTrade ? trade.profitLoss && trade.profitLoss < metrics.bestTrade
      ? trade.profitLoss : metrics.worstTrade : trade.profitLoss
  }
}
export const tradesReducerInitialState = {
  numberTrades: 0,
  maxTradeDuration: 1E20,
  totalTradeDuration: 0,
  winningTrades: 0,
  closedTrades: 0,
  bestTrade: null,
  worstTrade: null
}
export const tradesReducer = (state: any, action: any) => {
  switch (action.type) {
    case UPDATE_TRADES_STATISTICS:
      return {
        ...state,
        ...action.trades.reduce(tradesReducerCallback, tradesReducerInitialState),
      }
    default:
      throw new Error();
  }
}