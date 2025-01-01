from datetime import datetime
from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    """
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    """
    username: str


class User(BaseModel):
    """
    """
    username: str
    phone: str = None
    disabled: bool
    hashed_password: str
