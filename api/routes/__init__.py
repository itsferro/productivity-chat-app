from fastapi import APIRouter
from .auth import router as auth_router
from .conv import router as conversations_router
from .mess import router as messages_router
from .users import router as users_router
from .tasks import router as tasks_router
"""
"""


api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(conversations_router)
api_router.include_router(messages_router)
api_router.include_router(tasks_router)
