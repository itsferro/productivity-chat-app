from sqlalchemy import (
        Column, Integer, String, Boolean, ForeignKey, DateTime, Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db import Base
"""
"""


class User(Base):
    """
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    todoist_token = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_seen_online = Column(DateTime(timezone=True), nullable=True)
    conversations = relationship('ConversationParticipant', back_populates='user')
    sent_messages = relationship('Message', back_populates='sender', foreign_keys='Message.sender_id')
    received_messages = relationship('Message', back_populates='recipient', foreign_keys='Message.recipient_id')


class Conversation(Base):
    """
    """
    __tablename__ = 'conversations'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    priority = Column(Integer, default=0)
    tags = Column(String, nullable=True)
    labels = Column(String, nullable=True)
    participants = relationship('ConversationParticipant', back_populates='conversation')
    messages = relationship('Message', back_populates='conversation')


class ConversationParticipant(Base):
    """
    """
    __tablename__ = 'conversation_participants'

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    nickname = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    conversation = relationship('Conversation', back_populates='participants')
    user = relationship('User', back_populates='conversations')


class Message(Base):
    """
    """
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id', ondelete='CASCADE'), nullable=False)
    sender_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    recipient_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status = Column(String, nullable=False, default="sent")
    conversation = relationship('Conversation', back_populates='messages')
    sender = relationship('User', back_populates='sent_messages', foreign_keys=[sender_id])
    recipient = relationship('User', back_populates='received_messages', foreign_keys=[recipient_id])


class BannedUser(Base):
    """
    """
    __tablename__ = 'banned_users'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    banned_user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    banned_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Task(Base):
    """
    """
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    user = relationship('User', back_populates=None)

