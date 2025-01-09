from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from sqlalchemy.sql import func
from db import Base
"""
"""


class Conversation(Base):
    _tablename_ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    priority = Column(Integer, default=3)
    title = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    

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
        return f"<Conversation(id={self.id}, priority={self.priority})>"



