from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from sqlalchemy.sql import func
from api.base import Base
"""
"""


class ConversationParticipants(Base):
    """Association Table for Users and Conversations
    """
    __tablename__ = 'conversation_participants'

    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id', ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    joined_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

