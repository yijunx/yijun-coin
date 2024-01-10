import jwt
from app.models.user import UserInJWT

payload = UserInJWT(id="ads", name="haha").dict()
token = jwt.encode(payload=payload, key="1234")
print(f"{token=}")

user = UserInJWT(**jwt.decode(token, options={"verify_signature": False}))
print(user)