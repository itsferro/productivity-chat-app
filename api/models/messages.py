from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from sqlalchemy.sql import func
from api.base import Base
"""
"""


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id", ondelete='CASCADE'), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    content = Column(Text, nullable=False)
    status = Column(String, default="sent")
    todoist_task_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    conversation = relationship("Conversation", back_populates="messages")

    def create(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)

    def update(self, db: Session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.commit()
        db.refresh(self)

    def delete(self, db: Session):
        db.delete(self)
        db.commit()

    def _repr_(self):
        return f"<Message(id={self.id}, content={self.content[:20]}...)>"
