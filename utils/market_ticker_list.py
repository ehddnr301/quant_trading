import os
import requests


def fetch_krw_tickers():

    # API 서버 URL 및 엔드포인트 설정
    server_url = os.environ.get("UPBIT_OPEN_API_SERVER_URL")
    if not server_url:
        raise ValueError("환경 변수 'UPBIT_OPEN_API_SERVER_URL'이 설정되지 않았습니다.")

    url = server_url + "/v1/market/all"
    headers = {"accept": "application/json"}

    # API 요청 및 응답 처리
    res = requests.get(url, headers=headers)
    res.raise_for_status()  # 요청 실패 시 예외 발생

    ticker_list = res.json()

    # KRW로 시작하는 티커만 필터링하여 출력
    krw_tickers = [
        ticker for ticker in ticker_list if ticker["market"].startswith("KRW")
    ]
    return krw_tickers
