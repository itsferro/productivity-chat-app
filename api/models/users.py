from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from sqlalchemy.sql import func
from db import Base
"""
"""


class User(Base):
    """
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    todoist_token = Column(String, nullable=True)
    last_seen_online = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=True)
#    conversations = relationship("ConversationParticipant", back_populates="user")
#    sent_messages = relationship('Message', back_populates='sender', foreign_keys='Message.sender_id')
#    received_messages = relationship('Message', back_populates='recipient', foreign_keys='Message.recipient_id')
#    tasks = relationship("Task", back_populates="user")

    def create(self, db: Session):
        """Add this user to the database."""
        db.add(self)
        db.commit()
        db.refresh(self)

    def update(self, db: Session, **kwargs):
        """Update fields of this user and save changes."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.commit()
        db.refresh(self)

    def delete(self, db: Session):
        """Delete this user from the database."""
        db.delete(self)
        db.commit()

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
