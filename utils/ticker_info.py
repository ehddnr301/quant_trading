import os
import requests


def get_ticker_info(markets="KRW-BTC,KRW-ETH"):
    """
    Upbit API에서 특정 시장의 티커 정보를 가져오는 함수.

    Parameters:
        markets (str): 조회할 시장을 콤마로 구분하여 입력, 예: "KRW-BTC,KRW-ETH".

    Returns:
        list: 티커 정보가 담긴 JSON 응답을 리스트 형태로 반환.
    """
    server_url = os.environ.get("UPBIT_OPEN_API_SERVER_URL")
    if not server_url:
        raise ValueError("환경 변수 'UPBIT_OPEN_API_SERVER_URL'이 설정되지 않았습니다.")

    url = f"{server_url}/v1/ticker"
    params = {"markets": markets}
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


# # 사용 예시
# markets = "KRW-BTC,KRW-ETH"
# ticker_data = get_ticker_info(markets)
# print(ticker_data)
