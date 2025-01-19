from datetime import datetime
from pydantic import BaseModel
from typing import Optional
"""
"""


class MessIn(BaseModel):
    """
    """
    conversation_id: int
    content: str


class MessOut(BaseModel):
    """
    """
    id: int
    conversation_id: int
    sender_id: int
    content: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

class MessList(BaseModel):
    """
    """
    messages: list[MessOut]

class MessUpdate(BaseModel):
    """
    """
    content: Optional[str] = None
    status: Optional[str] = None
