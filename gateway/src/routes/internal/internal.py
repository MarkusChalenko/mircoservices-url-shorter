import httpx
from fastapi import APIRouter
from starlette.requests import Request

from auth.auth import user_dependency
from core.config import app_settings

internal_router = APIRouter(
    prefix="/internal",
    tags=["internal"]
)

url_shorter_microservice_url: str = app_settings.url_shorter_service_url
auth_microservice_url: str = app_settings.auth_service_url


@internal_router.get("/ping_auth")
async def ping_auth_service(request: Request, user: user_dependency):
    async with httpx.AsyncClient(base_url=auth_microservice_url) as client:
        response = await client.get('/ping', headers=request.headers)
        res = response.json()
    return res


@internal_router.get("/ping_shorter")
async def ping_shorter_service(request: Request, user: user_dependency):
    async with httpx.AsyncClient(base_url=url_shorter_microservice_url) as client:
        response = await client.get('/ping', headers=request.headers)
        res = response.json()
    return res
