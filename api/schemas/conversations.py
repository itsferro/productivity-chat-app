from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
"""
"""


class ConvOut(BaseModel):
    """
    """
    id: int
    partecepants: Optional[list[int]] = list[None]
    priority: str
    title: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None


class ConvList(BaseModel):
    """
    """
    conversations: list[ConvOut]


class ConvUpdate(BaseModel):
    """
    """
    partecepants: Optional[list[int]] = list[None]
    priority: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[datetime] = None
