import time
from dotenv import load_dotenv

load_dotenv(override=True)

from utils.market_ticker_list import fetch_krw_tickers
from utils.minutes_candle import get_minute_candle
from utils.orders import send_order_request
from utils.account_assets import get_upbit_assets

if __name__ == "__main__":
    # print(fetch_krw_tickers())
    # get_upbit_assets()
    # print(send_order_request("KRW-BTC", "ask", "market", volume="0.00005"))
    krw_tickers = fetch_krw_tickers()

    ticker_info_list = []

    for ticker in krw_tickers:
        time.sleep(0.08)
        ticker_info = get_minute_candle(market=ticker["market"], minute=1)

        ticker_info_list.append(ticker_info)

    sorted_ticker_info_list = sorted(
        ticker_info_list, key=lambda x: x["candle_acc_trade_volume"], reverse=True
    )

    for ticker_info in sorted_ticker_info_list:
        print(ticker_info)
        print()
