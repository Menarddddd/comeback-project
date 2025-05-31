from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import user
from ..models import User
from ..database import get_db
from ..services import user_service
from ..services.oauth2 import get_current_user


router = APIRouter(
    prefix="/user",
    tags=["User"] 
)



@router.get("/", status_code=status.HTTP_200_OK, response_model=List[user.UserResponseWithTweets])
def get_all_user(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return user_service.get_all_user(db)


@router.get("/{id}", response_model=user.UserResponseWithTweets)
def get_user_id(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return user_service.get_user_id(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=user.UserResponse)
def create_user(request: user.UserCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return user_service.create_user(request, db)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=user.UserResponse)
def update_user(id: int, request: user.UserUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return user_service.update_user(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return user_service.delete_user(id, db)



