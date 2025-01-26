from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from sqlalchemy.sql import func
from api.base import Base
from api.models.users import User
"""
"""


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    priority = Column(Integer, default=3)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")

    participants = relationship(
        "User",
        secondary="conversation_participants",
        back_populates="conversations",
    )
    

    def create(self, db: Session, participants: list[User]):
        for participant in participants:
            if not db.query(User).filter_by(id=participant.id).first():
                db.add(participant)
        self.participants.extend(participants)
        print(self)
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
        return f"<Conversation(id={self.id}, priority={self.priority})>"



