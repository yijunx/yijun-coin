from pydantic import BaseModel


class UserInJWT(BaseModel):
    id: str
    name: str
