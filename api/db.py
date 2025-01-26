from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.config import settings
from api.base import Base
from api.models import *
#from models.conversations import Conversation
#from models.users import User
#from models.relations_models import ConversationParticipants
#from models.messages import Message
"""
"""


SQLALCHEMY_DATABASE_URL = settings.database_url

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

def init_db():
    """
    """
    Base.metadata.create_all(bind=engine)
