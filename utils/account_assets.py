import jwt
import os
import requests
import uuid


def get_upbit_assets():
    # 페이로드 생성
    payload = {
        "access_key": os.environ["UPBIT_OPEN_API_ACCESS_KEY"],
        "nonce": str(uuid.uuid4()),
    }

    # JWT 토큰 생성 및 헤더 설정
    jwt_token = jwt.encode(payload, os.environ["UPBIT_OPEN_API_SECRET_KEY"])
    authorization = f"Bearer {jwt_token}"
    headers = {
        "Authorization": authorization,
    }

    # 요청 보내기
    response = requests.get(
        f"{os.environ['UPBIT_OPEN_API_SERVER_URL']}/v1/accounts", headers=headers
    )
    my_assets = response.json()

    # 자산 정보 출력
    # for asset in my_assets:
    #     print(asset["currency"], asset["balance"])

    return my_assets


# get_upbit_assets()
