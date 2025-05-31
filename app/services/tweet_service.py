from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import Tweet
from ..schemas import tweet


def get_all_tweet(db: Session):
    return db.query(Tweet).all()


def get_tweet_id(id: int, db: Session):
    tweet = db.query(Tweet).filter(Tweet.id == id).first()
    if not tweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tweet id {id} is not found!")
    return tweet


def create_tweet(request: tweet.TweetCreate, db: Session):
    tweet = Tweet(
        caption=request.caption,
        body=request.body,
        user_id = request.user_id
    )
    db.add(tweet)
    db.commit()
    return tweet


def update_tweet(id: int, request: tweet.TweetUpdate, db: Session):
    tweet = db.query(Tweet).filter(Tweet.id == id).first()
    if not tweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tweet not found!")
    
    updateTweet = request.model_dump(exclude_unset=True)
    for key, value in updateTweet.items():
        setattr(tweet, key, value)

    db.commit()
    db.refresh(tweet)
    return tweet


def remove_tweet(id: int, db: Session):
    tweet = db.query(Tweet).filter(Tweet.id == id).first()
    if not tweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tweet not found!")
    
    db.delete(tweet)
    db.commit()
    return "Successfuly deleted tweet!"