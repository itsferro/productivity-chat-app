from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db import get_db
from models.users import User
from datetime import datetime, timedelta
from utils.jwt import get_password_hash
from utils.jwt import authenticate_user
from utils.jwt import create_access_token
from utils.jwt import revoke_token
from utils.jwt import get_user
"""
"""


ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
db = {}
router = APIRouter(prefix="/auth")


@router.post("/signup")
async def user_signup(username: str, password: str, email: str, db: Session = Depends(get_db)):
    """
    """
    user = get_user(db, username)
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = get_password_hash(password)
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
        )
    user.create(db)
    return {
            "message": "User registered successfully",
            "user_data": user
            }

@router.post("/login")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"}
                )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {
            "access_token": access_token,
            "refresh_token": "<REFRESH_TOKEN>",
            "token_type": "Bearer",
            "expires_in": access_token_expires
            }


@router.post("/logout")
async def user_logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    """
    revoke_token(token)
    return {
            "message": "Logged out successfully"
            }
