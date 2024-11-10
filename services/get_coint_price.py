from utils.ticker_info import get_ticker_info


def get_price(ticker: str):
    return get_ticker_info(ticker)[0]["trade_price"]
