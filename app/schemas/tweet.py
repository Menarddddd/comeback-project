from typing import Optional
from pydantic import BaseModel


class TweetCreate(BaseModel):
    caption: str
    body: str
    user_id: int

class TweetResponse(BaseModel):
    caption: str
    body: str

    model_config = {
        "from_attributes": True
    }


class TweetResponseWithId(BaseModel):
    caption: str
    body: str
    user_id: int

    model_config = {
        "from_attributes": True
    }


class TweetUpdate(BaseModel):
    caption: Optional[str] = None
    body: Optional[str] = None
