# """Project entrypoint"""
# import multiprocessing
# from contextlib import asynccontextmanager
# from typing import AsyncContextManager
#
# import uvicorn
# from fastapi import FastAPI
# from fastapi.responses import ORJSONResponse
# from fastapi_cache import caches, close_caches
# from fastapi_cache.backends.redis import RedisCacheBackend, CACHE_KEY
# from fastapi_users import FastAPIUsers
#
# from auth import auth_backend
# from api.v1.base import api_router
# from auth.user_manager import get_user_manager
# from core.config import app_settings
# from models import User
# from schemas.user import UserRead, UserCreate
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncContextManager[None]:
#     redis = RedisCacheBackend(
#         f'redis://{app_settings.redis_host}:{app_settings.redis_port}'
#     )
#     caches.set(CACHE_KEY, redis)
#     try:
#         yield
#     finally:
#         await close_caches()
#
#
# app = FastAPI(
#     lifespan=lifespan,
#     title="URLshorter",
#     docs_url="/api/openapi",
#     openapi_url="/api/openapi.json",
#     default_response_class=ORJSONResponse,
#     redoc_url=None
# )
#
#
# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )
#
# app.include_router(api_router, prefix="/api/v1")
# app.include_router(fastapi_users.get_auth_router(auth_backend),
#                    prefix="/auth/jwt",
#                    tags=["auth"],
#                    )
# app.include_router(fastapi_users.get_register_router(UserRead, UserCreate),
#                    prefix="/auth",
#                    tags=["auth"],
#                    )
#
#
# @app.get("/")
# def root():
#     """root route"""
#     return "Hello"
#
#
# if __name__ == '__main__':
#     options = {
#         "host": f'{app_settings.app_host}',
#         "port": app_settings.app_port,
#         "workers": multiprocessing.cpu_count(),
#         "reload": app_settings.debug,
#     }
#
#     print(options)
#     uvicorn.run(
#         'main:app',
#         **options
#     )
from typing import Union


class Calculator:
    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments should be numeric type")
        return a + b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments should be numeric type")
        elif b == 0:
            raise ZeroDivisionError("Second argument cant be equal to zero")
        return a / b
