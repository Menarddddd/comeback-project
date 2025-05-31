from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import User
from ..schemas import user
from .hashing import get_password_hash, verify_password


def get_all_user(db: Session):
    return db.query(User).all()



def get_user_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User id {id} is not found!")
    return user



def create_user(request: user.UserCreate, db: Session):
    hashed_password = get_password_hash(request.password)

    user = User(
        first_name = request.first_name, 
        last_name = request.last_name,
        age = request.age,
        username = request.username,
        email = request.email,
        password = hashed_password
    )
    db.add(user)
    db.commit()
    return user



def update_user(id: int, request: user.UserUpdate, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User is not found!")
    
    userUpdate = request.model_dump(exclude_unset=True)
    for key, value in userUpdate.items():
        setattr(user, key, value)

    db.commit()
    return user



def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    
    db.delete(user)
    db.commit()
    return 