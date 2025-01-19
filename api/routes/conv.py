from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from db import get_db
from utils.jwt import get_current_user
from models.users import User
from models.conversations import Conversation
from models.relations_models import ConversationParticipants
from schemas.conversations import ConvIn, ConvOut, ConvDetails, ConvUpdate, ConvList, ConvMessages
"""
"""


router = APIRouter(
        prefix="/conversaitions",
        tags=['conversaitions']
        )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ConvOut)
def start_new_conversation(
        new_conv: ConvIn,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if not current_user.id in new_conv.participants:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="the current user has to be one of the partecepants",
                headers={"WWW-Authenticate": "Bearer"}
                )

    try:
        other_participant_id = next(id for id in new_conv.participants if id != current_user.id) #gets the other participant id.
        other_participants = db.query(User).filter(User.id == other_participant_id).first() #gets the other participant as a user.
        #removing the participants key and its value from the new_conv to not face errors when initializing the conv opject.
        new_conv = new_conv.dict()
        new_conv.pop("participants", None)
        #participants = [current_user, other_participants]
        conv = Conversation(**new_conv)
        #conv.participants.extend([currnet_user, other_participants])
        conv.create(db, [current_user, other_participants])
        return conv
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"ther's no user with this id [{other_participants_id}].",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.get("/", response_model=ConvList)
def retrieve_logged_in_user_conversations(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db),
        limit: int = 10,
        skip: int = 0,
        search: Optional[str] = None
        ):
    """
    """
    if limit <= 0 or skip < 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="limit param can't be less than or equal to zero, and skip param can't be less than zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    try:
        if search:
            conversations = db.query(Conversation).join(ConversationParticipants, Conversation.id == ConversationParticipants.conversation_id).filter(ConversationParticipants.user_id == current_user.id).filter(Conversation.title.contains(search)).limit(limit).offset(skip).all()
        else:
            conversations = db.query(Conversation).join(ConversationParticipants, Conversation.id == ConversationParticipants.conversation_id).filter(ConversationParticipants.user_id == current_user.id).limit(limit).offset(skip).all()
        return {
                "skiped": skip,
                "limit": limit,
                "search_value": search,
                "conversations": conversations
                }
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.get("/{id}/details", response_model=ConvDetails)
def retrieve_conversation_details(
        conv_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if conv_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="conversation id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    try:
        conversation = db.query(Conversation).join(ConversationParticipants, Conversation.id == ConversationParticipants.conversation_id).filter(ConversationParticipants.user_id == current_user.id).filter(Conversation.id == conv_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
                headers={"WWW-Authenticate": "Bearer"}
                )
    if conversation:
        print(conversation)
        return conversation
    else:
        print(conversation)
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"you're not part of a conversation by id={conv_id}",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.put("/{id}/details", response_model=ConvDetails)
def update_conversation_details(
        conv_id: int,
        updated_conv: ConvUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if conv_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="conversation id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    try:                                                                                                                            conversation = db.query(Conversation).join(ConversationParticipants, Conversation.id == ConversationParticipants.conversation_id).filter(ConversationParticipants.user_id == current_user.id).filter(Conversation.id == conv_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
                headers={"WWW-Authenticate": "Bearer"}
                )
    if conversation:
        print(conversation)
        if updated_conv.participants:
            participant_ids = [participant.id for participant in conversation.participants]
            print(participant_ids)
            for participant_id in updated_conv.participants:
                if participant_id not in participant_ids:  # Check if the participant is new
                    new_participant = db.query(User).filter(User.id == participant_id).first()
                    if new_participant:  # Ensure the participant exists in the database
                        conversation.participants.append(new_participant)
        try:
            update_data = updated_conv.dict(exclude_unset=True)
            update_data.pop("participants", None)
            conversation.updated_at = datetime.utcnow()
            conversation.update(db, **update_data)
            return conversation
        except Exception as e:
            print(e)
            raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Internal server error (database related)",
                    headers={"WWW-Authenticate": "Bearer"}
                    )
    else:
        print(conversation)
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"you're not part of a conversation by id={conv_id}",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.get("/{id}", response_model=ConvMessages)
def retrieve_conversation_content(
        id: int,
        current_user: User = Depends(get_current_user),                                                                             db: Session = Depends(get_db),
        limit: int = 10,                                                                                                            skip: int = 0,                                                                                                              search: Optional[str] = None
        ):
    """
    """
    if conv_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="conversation id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    if limit <= 0 or skip < 0:                                                                                                      raise HTTPException(                                                                                                                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,                                                                           detail="limit param can't be less than or equal to zero, and skip param can't be less than zero.",                          headers={"WWW-Authenticate": "Bearer"}                                                                                      )
    return {
            "conversation_id": 5,
            "participants": [1, 2],
            "messages": [
                {
                    "message_id": 99,
                    "sender_id": 1,
                    "recipient_id": 2,
                    "content": "Hello",
                    "timestamp": "2024-01-02T14:20:00Z",
                    "status": "delivered"
                    },
                {
                    "message_id": 100,
                    "sender_id": 2,
                    "recipient_id": 1,
                    "content": "Hey! All good?",
                    "timestamp": "2024-01-02T14:21:00Z",
                    "status": "read"
                    }
                ]
            }


@router.delete("/{id}")
def delete_conversation(
        conv_id: int,
        current_user: User = Depends(get_current_user),                                                                             db: Session = Depends(get_db)
        ):
    """
    """
    if conv_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="conversation id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    try:
        conversation = db.query(Conversation).join(ConversationParticipants, Conversation.id == ConversationParticipants.conversation_id).filter(ConversationParticipants.user_id == current_user.id).filter(Conversation.id == conv_id).first()
        try:
            conversation.delete(db)
            return {
                    "message": "conversation deleted successfully"
                    }
        except Exception as e:
            print(e)
            raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Internal server error",
                    headers={"WWW-Authenticate": "Bearer"}
                    )
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
                headers={"WWW-Authenticate": "Bearer"}
                )
