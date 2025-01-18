from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
from base import Base
from models.conversations import Conversation
from models.users import User
from models.relations_models import ConversationParticipants
"""
"""



SQLALCHEMY_DATABASE_URL = settings.dev_database_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {},
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Base = declarative_base()

def init_db():
    """
    """
    Base.metadata.create_all(bind=engine)
