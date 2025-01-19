from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from db import get_db
from utils.jwt import get_current_user
from models.users import User
from models.conversations import Conversation
from models.relations_models import ConversationParticipants
from models.messages import Message
from schemas.messages import MessIn, MessOut, MessUpdate
"""
"""


router = APIRouter(
        prefix="/messages",
        tags=['Messages']
        )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MessOut)
def send_message(
        new_mess: MessIn,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    if db.query(Conversation).join(ConversationParticipants, Conversation.id == ConversationParticipants.conversation_id).filter(ConversationParticipants.user_id == current_user.id).filter(Conversation.id == new_mess.conversation_id).first():
        new_mess_data = new_mess.dict()
        new_mess_data["sender_id"] = current_user.id
        message = Message(**new_mess_data)
        try:
            message.create(db)
            return message
        except Exception as e:
            print(e)
            raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Internal server error",
                    headers={"WWW-Authenticate": "Bearer"}
                    )
    else:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"you're not part of a conversation by id={new_mess.conversation_id}",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.get("/{id}", response_model=MessOut)
def retrieve_message_details(
        mess_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if mess_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="conversation id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    try:
        message = db.query(Message).filter(Message.id == mess_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
                headers={"WWW-Authenticate": "Bearer"}
                )
    if message:
        print(message)
        return message
    else:
        print(message)
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"either message by id={mess_id} does not exist or you're not part of it is conversation",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.put("/{id}", response_model=MessOut)
def edit_message(
        mess_id: int,
        updated_mess: MessUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if mess_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="conversation id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    if updated_mess:
        try:
            message = db.query(Message).filter(Message.id == mess_id).first()
        except Exception as e:
            print(e)
            raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Internal server error",
                    headers={"WWW-Authenticate": "Bearer"}
                    )
        if message and message.sender_id is current_user.id:
            print(message)
            message.updated_at = datetime.utcnow()
            message.update(db, **updated_mess.dict(exclude_unset=True))
            return message
        else:
            print(message)
            raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"you're not the sender of this message, or either the message by id={mess_id} does not exist or you're not part of it is conversation",
                    headers={"WWW-Authenticate": "Bearer"}
                    )
    else:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"you either have to provide a content or status or both in the payload of you'r request",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.delete("/{id}")
def delete_message(
        mess_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if mess_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="conversation id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    try:
        message = db.query(Message).filter(Message.id == mess_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
                headers={"WWW-Authenticate": "Bearer"}
                )
    if message and message.sender_id is current_user.id:
        print(message)
        try:
            message.delete(db)
            return {
                    "message": "message deleted successfully"
                    }
        except Exception as e:
            print(message)
            raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Internal server error",
                    headers={"WWW-Authenticate": "Bearer"}
                    )
    else:
        print(message)
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"you're not the sender of this message, or either the message by id={mess_id} does not exist or you're not part of it is conversation",
                headers={"WWW-Authenticate": "Bearer"}
                )
