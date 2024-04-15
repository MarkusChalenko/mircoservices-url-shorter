import httpx
from fastapi import APIRouter
from starlette.requests import Request

from auth.auth import user_dependency

internal_router = APIRouter(
    prefix="/internal",
    tags=["internal"]
)


@internal_router.get("/ping_auth")
async def ping_auth_service(request: Request, user: user_dependency):
    async with httpx.AsyncClient() as client:
        response = await client.get('http://auth:8001/ping', headers=request.headers)
        res = response.json()
    return res


@internal_router.get("/ping_shorter")
async def ping_shorter_service(request: Request, user: user_dependency):
    async with httpx.AsyncClient() as client:
        response = await client.get('http://url-shorter:8002/ping', headers=request.headers)
        res = response.json()
    return res
