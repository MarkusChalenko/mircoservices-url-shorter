from fastapi import APIRouter

from routes.internal.internal import internal_router
from routes.token.token import token_router
from routes.url_shorter.url_shorter_routes import url_shorter_router
from routes.user.user_routes import user_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/api/v1")
api_router.include_router(token_router, prefix="/api/v1")
api_router.include_router(url_shorter_router, prefix="/api/v1")
api_router.include_router(internal_router, prefix="/api/v1")
