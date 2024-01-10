from pydantic import BaseModel


class UserInJWT(BaseModel):
    id: int
    name: str
    email: str
