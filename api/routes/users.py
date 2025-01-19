from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional, Union
from datetime import datetime
from db import get_db
from utils.jwt import get_current_user, hash_password, verify_password
from models.users import User
from schemas.users import UsersList, UserProfile, UserOut, UserUpdate
"""
"""


router = APIRouter(
        prefix="/users",
        tags=['Users']
        )


@router.get("/", response_model=UsersList)
def retrieve_users(
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
            users = db.query(User).filter(User.username.contains(search)).limit(limit).offset(skip).all()
        else:
            users = db.query(User).limit(limit).offset(skip).all()
        return {
                "skipped": skip,
                "limit": limit,
                "search_value": search,
                "users": users
                }
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.get("/{id}/status")
def check_online_offline_status(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    still under development
    """
    return {
            "message": "offline",
            "last_seen": "2024-01-02T12:00:00Z"
            }


@router.get("/{id}", response_model=Union[UserProfile, UserOut])
def retrieve_user_profile_detail(
        user_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """

    if user_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="user id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )

    try:
        user = db.query(User).filter(User.id == user_id).first()
        if current_user.id is user_id:
            return UserProfile.from_orm(user)
        else:
            return UserOut.from_orm(user)
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ther's no user with this id.",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.put("/{id}", response_model=UserProfile)
def update_user_profile_detail(
        user_id: int,
        updated_user: UserUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if user_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="user id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )

    if user_id is current_user.id:
        if updated_user.password is None:
            updated_user.password = current_user.password
        elif not verify_password(updated_user.password, current_user.password):
            updated_user.password = hash_password(updated_user.password)
        else:
            updated_user.password = current_user.password

        try:
            update_data = updated_user.dict(exclude_unset=True)
            current_user.updated_at = datetime.utcnow()
            current_user.update(db, **update_data)
            return current_user
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error (database related)",
                headers={"WWW-Authenticate": "Bearer"}
                )
    else:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="you're only allowed to edit your own profile, You are not allowed to edit another user's profile.",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.delete("/{id}")
def delete_user(
        user_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if user_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="user id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    if user_id is current_user.id:
        try:
            current_user.delete(db)
            return {
                    "message": "user deleted successfully"
                    }
        except Exception as e:
            print(e)
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="ther's no user with this id.",
                    headers={"WWW-Authenticate": "Bearer"}
                    )
    else:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="you're only allowed to delete your own profile, You are not allowed to delete another user's profile.",
                headers={"WWW-Authenticate": "Bearer"}
                )


@router.post("/bans")
def user_bans_list_control(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    still under development
    """
    return {
            "message": "you successfully added user 6 to your 'benned users' list"
            }
