from typing import List
from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import tweet
from ..services.oauth2 import get_current_user  
from ..services import tweet_service

router = APIRouter(
    prefix="/tweet",    
    tags=["Tweet"]
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[tweet.TweetResponseWithId])
def get_all_tweet(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return tweet_service.get_all_tweet(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=tweet.TweetResponseWithId)
def get_tweet_id(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return tweet_service.get_tweet_id(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=tweet.TweetResponse)
def create_tweet(request: tweet.TweetCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return tweet_service.create_tweet(request, db)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=tweet.TweetResponse)
def update_tweet(id: int, request: tweet.TweetUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return tweet_service.update_tweet(id, request, db)
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_tweet(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return tweet_service.remove_tweet(id, db)

