from fastapi import APIRouter, Form, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..models import User
from ..database import get_db
from ..schemas import token
from ..schemas.login import LoginCreate
from ..services.hashing import verify_password
from ..services.oauth2 import create_access_token


router = APIRouter(
    tags=["Login"]
)

@router.post("/login", status_code=status.HTTP_200_OK, response_model=token.Token)
def login(username = Form(...), password = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No username found!")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username or password is not correct!")

    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}
