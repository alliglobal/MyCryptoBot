from datetime import datetime

import pandas as pd
import pytz
from pandas import Timestamp

sample_structured_data = [
    dict(
        exchange_id="binance",
        symbol_id="BTCUSDT",
        open_time=datetime(2019, 9, 2, 10, tzinfo=pytz.utc),
        close_time=datetime(2019, 9, 1, 11, tzinfo=pytz.utc),
        interval="1h",
        open=1,
        high=1,
        low=1,
        close=1,
        volume=1,
        quote_volume=1,
        trades=1,
        taker_buy_asset_volume=1,
        taker_buy_quote_volume=1,
    )
]


data = pd.DataFrame(
    [
        {
            "open_time": Timestamp("2023-09-01 14:00:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 13:59:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 7614,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
        },
        {
            "open_time": Timestamp("2023-09-01 14:05:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:04:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 7614,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
        },
        {
            "open_time": Timestamp("2023-09-01 14:10:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:09:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 7614,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
        },
        {
            "open_time": Timestamp("2023-09-01 14:15:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:14:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 7614,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
        },
        {
            "open_time": Timestamp("2023-09-01 14:20:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:19:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 7614,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
        },
        {
            "open_time": Timestamp("2023-09-01 14:25:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:29:59.999000+0000", tz="UTC"),
            "open": 55388.95,
            "high": 55569.95,
            "low": 55388.95,
            "close": 55552.4,
            "volume": 149.363426,
            "quote_volume": 8288967.03877351,
            "trades": 5260,
            "taker_buy_asset_volume": 82.67909,
            "taker_buy_quote_volume": 4588065.23181743,
        },
        {
            "open_time": Timestamp("2023-09-01 14:30:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:34:59.999000+0000", tz="UTC"),
            "open": 55550.89,
            "high": 56087.68,
            "low": 55550.89,
            "close": 55932.48,
            "volume": 692.924319,
            "quote_volume": 38726480.58078431,
            "trades": 16507,
            "taker_buy_asset_volume": 411.223017,
            "taker_buy_quote_volume": 22979821.33981915,
        },
        {
            "open_time": Timestamp("2023-09-01 14:35:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:39:59.999000+0000", tz="UTC"),
            "open": 55932.48,
            "high": 56333.0,
            "low": 55932.48,
            "close": 56264.93,
            "volume": 603.660118,
            "quote_volume": 33896505.6971466,
            "trades": 14656,
            "taker_buy_asset_volume": 356.915883,
            "taker_buy_quote_volume": 20037884.70780964,
        },
        {
            "open_time": Timestamp("2023-09-01 14:40:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:44:59.999000+0000", tz="UTC"),
            "open": 56260.11,
            "high": 56317.43,
            "low": 56118.31,
            "close": 56168.82,
            "volume": 370.500359,
            "quote_volume": 20822485.25288953,
            "trades": 8616,
            "taker_buy_asset_volume": 178.075904,
            "taker_buy_quote_volume": 10007121.78892216,
        },
        {
            "open_time": Timestamp("2023-09-01 14:45:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:49:59.999000+0000", tz="UTC"),
            "open": 56168.82,
            "high": 56269.99,
            "low": 56080.96,
            "close": 56191.11,
            "volume": 324.51432,
            "quote_volume": 18225087.41727558,
            "trades": 8352,
            "taker_buy_asset_volume": 145.064381,
            "taker_buy_quote_volume": 8146012.47892439,
        },
        {
            "open_time": Timestamp("2023-09-01 14:50:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:54:59.999000+0000", tz="UTC"),
            "open": 56191.11,
            "high": 56200.0,
            "low": 56107.98,
            "close": 56145.0,
            "volume": 254.091606,
            "quote_volume": 14265787.89818125,
            "trades": 6455,
            "taker_buy_asset_volume": 134.1124,
            "taker_buy_quote_volume": 7529521.30623853,
        },
        {
            "open_time": Timestamp("2023-09-01 14:55:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 14:59:59.999000+0000", tz="UTC"),
            "open": 56145.0,
            "high": 56211.7,
            "low": 56106.97,
            "close": 56182.11,
            "volume": 270.145731,
            "quote_volume": 15171017.18758856,
            "trades": 7707,
            "taker_buy_asset_volume": 168.231118,
            "taker_buy_quote_volume": 9447425.0774598,
        },
        {
            "open_time": Timestamp("2023-09-01 15:00:00+0000", tz="UTC"),
            "close_time": Timestamp("2023-09-01 15:04:59.999000+0000", tz="UTC"),
            "open": 56182.12,
            "high": 56299.78,
            "low": 56172.09,
            "close": 56289.89,
            "volume": 298.797415,
            "quote_volume": 16804824.55255641,
            "trades": 9000,
            "taker_buy_asset_volume": 139.83665,
            "taker_buy_quote_volume": 7864202.02549528,
        },
    ]
)


STRATEGIES = {
    'BollingerBands': {
        "name": "Bollinger Bands",
        "params": ["ma", "sd"],
        "optional_params": []
    },
    'MachineLearning': {
        "name": "Machine Learning",
        "params": [
            "estimator",
        ],
        "optional_params": [
            "lag_features",
            "rolling_features",
            "excluded_features",
            "nr_lags",
            "windows",
            "test_size",
            "degree",
            "print_results"
        ]
    },
    'Momentum': {
        "name": "Momentum",
        "params": ["window"],
        "optional_params": []
    },
    'MovingAverageConvergenceDivergence': {
        "name": "Moving Average Convergence Divergence",
        "params": ["window_slow", "window_fast", "window_signal"],
        "optional_params": []
    },
    'MovingAverage': {
        "name": "Moving Average",
        "params": ["ma"],
        "optional_params": ["moving_av"]
    },
    'MovingAverageCrossover': {
        "name": "Moving Average Crossover",
        "params": ["SMA_S", "SMA_L"],
        "optional_params": ["moving_av"]
    },
}

