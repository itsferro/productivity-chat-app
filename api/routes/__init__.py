from fastapi import APIRouter
from routes.auth import router as auth_router
from routes.conv import router as conversations_router
from routes.mess import router as messages_router
from routes.users import router as users_router
from routes.tasks import router as tasks_router
"""
"""


api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(conversations_router)
api_router.include_router(messages_router)
api_router.include_router(tasks_router)
