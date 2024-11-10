import os
import requests
from datetime import datetime


def get_minute_candle(
    market="KRW-BTC",
    minute=1,
    to_time: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
):
    server_url = os.environ.get("UPBIT_OPEN_API_SERVER_URL")
    if not server_url:
        raise ValueError("환경 변수 'UPBIT_OPEN_API_SERVER_URL'이 설정되지 않았습니다.")

    url = server_url + "/v1/candles/minutes/1"
    params = {"market": market, "count": minute, "to": to_time}
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()[0] if response.json() else None
    else:
        print(f"Error: {response.status_code}")
        return None
