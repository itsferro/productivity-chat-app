from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from schemas.users import UserOut
from schemas.messages import MessOut, MessList
"""
"""


class ConvIn(BaseModel):
    """
    """
    participants: list[int]
    priority: Optional[str] = None
    title: Optional[str] = None


class ConvOut(BaseModel):
    """
    """
    id: int
    title: Optional[str] = None
    participants: list[UserOut]
    priority: Optional[int] = None
    updated_at: Optional[datetime] = None

class ConvDetails(ConvOut):
    """
    """
    created_at: datetime


class ConvList(BaseModel):
    """
    """
    skipped: int
    limit: int
    search_value: Optional[str]
    conversations: list[ConvOut]


class ConvUpdate(BaseModel):
    """
    """
    title: Optional[str] = None
    participants: Optional[list[int]] = list[None]
    priority: Optional[str] = None


class ConvMessages(BaseModel):
    """
    """
    id: int
    title: Optional[str] = None
    participants: list[UserOut]
    conv_messages: MessList
