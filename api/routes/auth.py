
from fastapi import APIRouter
"""
"""


router = APIRouter(prefix="/auth")


@router.post("/signup")
def user_signup():
    """
    """
    return {
            "message": "User registered successfully",
            "user_id": 1
            }

@router.post("/login")
def user_login():
    """
    """
    return {
            "access_token": "<JWT_ACCESS_TOKEN>",
            "refresh_token": "<REFRESH_TOKEN>",
            "token_type": "Bearer",
            "expires_in": 3600
            }


@router.post("/logout")
def user_logout():
    """
    """
    return {
            "message": "Logged out successfully"
            }
