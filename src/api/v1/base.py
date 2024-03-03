from fastapi import APIRouter
from .short_url import router as short_url_router

api_router = APIRouter()

api_router.include_router(short_url_router, prefix='')