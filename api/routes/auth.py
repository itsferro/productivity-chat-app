from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from db import get_db
from utils import jwt
from models import users
from schemas.auth import TokenOut
from schemas.users import UserIn, UserOut
"""
"""


router = APIRouter(
        prefix="/auth",
        tags=['Authentication']
        )

#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def user_signup(new_user: UserIn, db: Session = Depends(get_db)):
    """
    """
    user = jwt.get_user(db, new_user.username)
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = jwt.hash_password(new_user.password)
    new_user.password = hashed_password
    try:
        user = users.User(**new_user.dict())
        user.create(db)
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
                headers={"WWW-Authenticate": "Bearer"}
                )
    return user


@router.post("/login", response_model=TokenOut)
def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    """
    user = jwt.authenticate_user(db, user_credentials.username, user_credentials.password)

    if not user:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"}
                )

    access_token = jwt.create_access_token(
        data={"sub": user.username}, expires_delta=None)

    return {
            "access_token": access_token,
            "token_type": "Bearer",
            }


#@router.post("/logout")
#def user_logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#    """
#    """
#    jwt.revoke_token(token)
#    return {
#            "message": "Logged out successfully"
#            }
