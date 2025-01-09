from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from db import get_db
from config import settings
from schemas.auth import TokenData
from models.users import User
"""
"""


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

#revoked_tokens = set()


def verify_password(plain_password: str, hashed_password: str):
    """
    """
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str):
    """
    """
    return pwd_context.hash(password)


def get_user(db, username: str):
    """
    """
    try:
        user = db.query(User).filter(User.username == username).first()
        return user
    except Exception as e:
        print(e)
        return None


def authenticate_user(db, username: str, password: str):
    """
    """
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    return user


def create_access_token(data: TokenData, expires_delta: timedelta):
    """
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    """
    credential_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"}
            )
    # Check if token is revoked
#    if token in revoked_tokens:
#        raise HTTPException(
#                status_code=status.HTTP_401_UNAUTHORIZED,
#            detail="Token has been revoked",
#            headers={"WWW-Authenticate": "Bearer"}
#        )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
    except JWTError:
        raise credential_exception

    user = get_user(db, username=username)
    if user is None:
        raise credential_exception

    return user


#async def revoke_token(token):
#    """
#    """
#    revoked_tokens.add(token)
#    return True
