from typing import List

import httpx
from fastapi import APIRouter
from starlette import status
from starlette.requests import Request

from auth.auth import user_dependency
from core.config import app_settings
from schemas.url_shorter_microservice.url_shorter import Url, ShortedUrl, UpdateShortedUrl

url_shorter_router = APIRouter(
    prefix="/url-shorter",
    tags=['url_shorter_microservice']
)

url_shorter_microservice_url: str = app_settings.url_shorter_service_url


@url_shorter_router.get("/", status_code=status.HTTP_200_OK, response_model=list[ShortedUrl])
async def get_short_urls() -> list[ShortedUrl]:
    async with httpx.AsyncClient(base_url=url_shorter_microservice_url) as client:
        response = await client.get(f"/api/v1/short_url/")
        shorted_urls: List[ShortedUrl] = response.json()

    return shorted_urls


@url_shorter_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShortedUrl)
async def create_short_url(request: Request, user: user_dependency, url_to_short: Url) -> ShortedUrl:
    async with httpx.AsyncClient(base_url=url_shorter_microservice_url) as client:
        response = await client.post(f"/api/v1/short_url/",
                                     json=url_to_short.json(),
                                     headers=request.headers)
        created_shorted_url = response.json()

    return created_shorted_url


@url_shorter_router.put("/", status_code=status.HTTP_200_OK, response_model=ShortedUrl)
async def update_short_url(request: Request, user: user_dependency, short_url_id: str, short_url: UpdateShortedUrl) -> ShortedUrl:
    async with httpx.AsyncClient(base_url=url_shorter_microservice_url) as client:
        response = await client.put(f"/api/v1/short_url/{short_url_id}",
                                    json=short_url.dict(),
                                    headers=request.headers)
        shorted_url: ShortedUrl = response.json()

    return shorted_url


@url_shorter_router.delete("/", status_code=status.HTTP_200_OK)
async def delete_short_url(request: Request, user: user_dependency, short_url_id: str) -> dict:
    async with httpx.AsyncClient(base_url=url_shorter_microservice_url) as client:
        await client.delete(f"/api/v1/short_url/{short_url_id}",
                            headers=request.headers)

    return {"message": f"URL with id:{short_url_id} deleted successfully."}
