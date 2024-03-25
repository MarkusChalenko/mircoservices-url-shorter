"""Project entrypoint"""
import multiprocessing
from contextlib import asynccontextmanager
from typing import AsyncContextManager, Optional

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import ORJSONResponse
from fastapi_cache import caches, close_caches
from fastapi_cache.backends.redis import RedisCacheBackend, CACHE_KEY

from api.v1.auth import auth_router
from api.v1.user import user_router
from core.config import app_settings
from db.db import db_dependency


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncContextManager[None]:
    redis = RedisCacheBackend(
        f'redis://{app_settings.redis_host}:{app_settings.redis_port}'
    )
    caches.set(CACHE_KEY, redis)
    try:
        yield
    finally:
        await close_caches()


app = FastAPI(
    lifespan=lifespan,
    title="URLshorter-auth",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    redoc_url=None
)


app.include_router(auth_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")


@app.get("/")
def root():
    """root route"""
    return "Hello"


if __name__ == '__main__':
    options = {
        "host": f'{app_settings.app_host}',
        "port": app_settings.app_port,
        "workers": multiprocessing.cpu_count(),
        "reload": app_settings.debug,
    }

    print(options)
    uvicorn.run(
        'main:app',
        **options
    )