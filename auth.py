import jwt  # PyJWT
import uuid


payload = {
    "access_key": ACCESS_KEY,
    "nonce": str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, SECRET_KEY)
authorization_token = "Bearer {}".format(jwt_token)

print(authorization_token)
