from fastapi import APIRouter, Depends
from utils.jwt import get_current_user
from models.users import User
from db import get_db
from sqlalchemy.orm import Session
"""
"""


router = APIRouter(
        prefix="/users",
        tags=['Users'])


@router.get("/")
def retrieve_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {current_user}
    """
    return {
            "users": [
                {
                    "user_id": 1,
                    "username": "user123",
                    "email": "user123@example.com",
                    "created_at": "2024-01-02T12:00:00Z",
                    "phone": "+218943717245",
                    "todoist_token": "khugvjhfgjhvkjh",
                    "last_seen_online": "2024-01-02T12:00:00Z"
                    }
                ]
            }
            """


@router.get("/{id}")
def retrieve_user_profile_detail(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {
            "user_id": 1,
            "username": "user123",
            "email": "user123@example.com",
            "created_at": "2024-01-02T12:00:00Z",
            "phone": "+218943717245",
            "todoist_token": "khugvjhfgjhvkjh",
            "last_seen_online": "2024-01-02T12:00:00Z",
            "conversations_count": 20,
            "banned_users": [
                {
                    "user_id": 1,
                    "banned_at": "2024-01-02T12:00:00Z"
                    },
                {
                    "user_id": 1,
                    "banned_at": "2024-01-02T12:00:00Z"
                    }
                ]
            }


@router.put("/{id}")
def update_user_profile_detail(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {"user_id": 1,
            "username": "user123",
            "email": "user123@example.com",
            "created_at": "2024-01-02T12:00:00Z",
            "phone": "+218943717245",
            "todoist_token": "khugvjhfgjhvkjh",
            "last_seen_online": "2024-01-02T12:00:00Z",
            "conversations_count": 20,
            "banned_users": [
                {
                    "user_id": 1,
                    "banned_at": "2024-01-02T12:00:00Z"
                    },
                {
                    "user_id": 1,
                    "banned_at": "2024-01-02T12:00:00Z"
                    }
                ]
            }


@router.get("/{id}/status")
def check_online_offline_status(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {
            "message": "offline",
            "last_seen": "2024-01-02T12:00:00Z"
            }


@router.delete("/{id}")
def delete_user(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
     return {
             "message": "user deleted successfully"
             }


@router.post("/bans")
def user_bans_list_control(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {
            "message": "you successfully added user 6 to your 'benned users' list"
            }
