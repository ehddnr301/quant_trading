import time

from utils.market_ticker_list import fetch_krw_tickers
from utils.minutes_candle import get_minute_candle
from utils.days_candle import get_daily_candle


def get_minute_candle_list():
    krw_tickers = fetch_krw_tickers()

    ticker_info_list = []

    for ticker in krw_tickers:
        time.sleep(0.08)
        # ticker_info = get_minute_candle(market=ticker["market"], minute=1)
        ticker_info = get_daily_candle(market=ticker["market"], count=1)
        ticker_info_list.append(ticker_info)

    sorted_ticker_info_list = sorted(
        ticker_info_list, key=lambda x: x["candle_acc_trade_volume"], reverse=True
    )

    return sorted_ticker_info_list
