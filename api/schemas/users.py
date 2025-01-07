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
    email: Optional[str] = None
    phone: Optional[str] = None
    last_seen_online: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserProfile(UserOut):
    """
    """
    todoist_token: str
    created_at: datetime
    updated_at: datetime
