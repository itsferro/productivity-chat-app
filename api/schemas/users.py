from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
"""
"""


class UserIn(BaseModel):
    """
    """
    username: str
    password: str
    email: Optional[EmailStr] = None


class UserOut(BaseModel):
    """
    """
    id: int
    username: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    last_seen_online: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserProfile(UserOut):
    """
    """
    todoist_token: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class UsersList(BaseModel):
    """
    """
    skiped: int
    limit: int
    search_value: Optional[str]
    users: list[UserOut]


class UserUpdate(BaseModel):
    """
    """
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    todoist_token: Optional[str] = None
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        from_attributes = True
