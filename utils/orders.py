import os
import jwt
import hashlib
import requests
import uuid
from urllib.parse import urlencode, unquote


def send_order_request(
    market="KRW-BTC", side="bid", ord_type="price", price=None, volume=None
):
    # Set up parameters for the order based on order type
    params = {
        "market": market,
        "side": side,
        "ord_type": ord_type,
    }

    # Add price or volume based on order type
    if side == "bid" and price:
        params["price"] = price
    elif side == "ask" and volume:
        params["volume"] = volume

    print(params)
    # Encode and hash the query string
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")
    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    # Set up the payload and headers
    payload = {
        "access_key": os.environ["UPBIT_OPEN_API_ACCESS_KEY"],
        "nonce": str(uuid.uuid4()),
        "query_hash": query_hash,
        "query_hash_alg": "SHA512",
    }
    jwt_token = jwt.encode(payload, os.environ["UPBIT_OPEN_API_SECRET_KEY"])
    authorization = f"Bearer {jwt_token}"
    headers = {
        "Authorization": authorization,
    }

    # Send the request and return the response
    response = requests.post(
        f"{os.environ['UPBIT_OPEN_API_SERVER_URL']}/v1/orders",
        json=params,
        headers=headers,
    )
    return response.json()
