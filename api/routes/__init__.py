__all__ = ['auth', 'conv', 'mess', 'tasks', 'users']

from fastapi import APIRouter
from api.routes.auth import router as auth_router
from api.routes.conv import router as conversations_router
from api.routes.mess import router as messages_router
from api.routes.users import router as users_router
from api.routes.tasks import router as tasks_router
"""
"""


api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(conversations_router)
api_router.include_router(messages_router)
api_router.include_router(tasks_router)
