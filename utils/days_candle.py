import requests
from datetime import datetime


def get_daily_candle(
    market="KRW-BTC", count=1, to_time=None, converting_price_unit="KRW"
):
    """
    KRW-BTC 시장의 일봉 데이터를 조회하는 함수.

    Parameters:
    - market (str): 조회할 시장 (기본값은 "KRW-BTC")
    - count (int): 조회할 일봉의 개수 (기본값은 1)
    - to_time (str): 조회 종료 시각 (기본값은 현재 시간)
    - converting_price_unit (str): 가격 변환 단위 (기본값은 "KRW")

    Returns:
    - list: 일봉 데이터의 JSON 형식 리스트
    """
    if to_time is None:
        to_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    url = "https://api.upbit.com/v1/candles/days"
    params = {
        "market": market,
        "count": count,
        "to": to_time,
        "convertingPriceUnit": converting_price_unit,
    }
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        candles = response.json()
        for candle in candles:
            print(candle["candle_acc_trade_volume"] * candle["trade_price"])
        return candles
    else:
        print(f"Error: {response.status_code}")
        return None


# 함수 사용 예시
# print(get_daily_candle())
