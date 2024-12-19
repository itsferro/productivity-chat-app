from fastapi import APIRouter
from .auth import router as auth_router
from .conv import router as conversations_router
"""
"""


api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(conversations_router)
