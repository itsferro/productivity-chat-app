from datetime import datetime
from pydantic import BaseModel, EmailStr
"""
"""


class TokenOut(BaseModel):
    """
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    """
    sub: str
    exp: datetime


class Pyuser(BaseModel):
    """
    """
    username: str
    email: str = None
    phone: str = None
    hashed_password: str
    disabled: bool = False
    todoist_token: str = None
    last_seen_online: datetime = None
    created_at: datetime
    updated_at: datetime = None
