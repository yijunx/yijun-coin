from pydantic import BaseModel


class UserInJWT(BaseModel):
    id: int
    name: str
    email: str

    def __repr__(self) -> str:
        return f"id: {self.id} name: {self.name} email: {self.email}"
    
    class Config:
        orm_mode = True

