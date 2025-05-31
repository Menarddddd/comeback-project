
from typing import List, Optional
from pydantic import BaseModel
from .tweet import TweetResponse


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    model_config = {
        "from_attributes": True
    }

class UserResponseWithTweets(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    tweets: List[TweetResponse]

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


