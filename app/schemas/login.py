from pydantic import BaseModel


class LoginCreate(BaseModel):
    username: str
    password: str

    