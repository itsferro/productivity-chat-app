from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from utils.jwt import get_password_hash
from utils.jwt import authenticate_user
from utils.jwt import create_access_token
from utils.jwt import revoke_token
"""
"""


ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
db = {}
router = APIRouter(prefix="/auth")


@router.post("/signup")
async def user_signup(username: str, password: str):
    """
    """
    if username in db:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = get_password_hash(password)
    db[username] = {
        "username": username,
        "hashed_password": hashed_password,
        "disabled": False
    }
    return {
            "message": "User registered successfully"
            }

@router.post("/login")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
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
async def user_logout(token: str = Depends(oauth2_scheme)):
    """
    """
    revoke_token(token)
    return {
            "message": "Logged out successfully"
            }
