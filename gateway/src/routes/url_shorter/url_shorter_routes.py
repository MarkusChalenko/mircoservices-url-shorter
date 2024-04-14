from typing import List

import httpx
from fastapi import APIRouter
from starlette import status

from auth.auth import user_dependency
from core.config import app_settings
from schemas.url_shorter_microservice.url_shorter import Url, ShortedUrl, UpdateShortedUrl

url_shorter_router = APIRouter(
    prefix="/url-shorter",
    tags=['url_shorter_microservice']
)

url_shorter_microservice_url: str = app_settings.url_shorter_service_url


def endpoint(endp: str) -> str:
    return url_shorter_microservice_url + endp


@url_shorter_router.get("/", status_code=status.HTTP_200_OK, response_model=list[ShortedUrl])
async def get_short_urls() -> list[ShortedUrl]:
    print(endpoint(f"/api/v1/short_url/"))
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint(f"/api/v1/short_url/"))
        shorted_urls: List[ShortedUrl] = response.json()

    return shorted_urls


@url_shorter_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShortedUrl)
async def create_short_url(user: user_dependency, url_to_short: Url) -> ShortedUrl:
    async with httpx.AsyncClient() as client:
        print(url_to_short.json())
        response = await client.post(endpoint(f"/api/v1/short_url/"),
                                     json=url_to_short.json())
        created_shorted_url = response.json()
        print(created_shorted_url)

    return created_shorted_url


@url_shorter_router.put("/", status_code=status.HTTP_200_OK, response_model=ShortedUrl)
async def update_short_url(user: user_dependency, short_url_id: str, short_url: UpdateShortedUrl) -> ShortedUrl:
    async with httpx.AsyncClient() as client:
        response = await client.put(endpoint(f"/api/v1/short_url/{short_url_id}"),
                                    json=short_url.dict())
        shorted_url: ShortedUrl = response.json()

    return shorted_url


@url_shorter_router.delete("/", status_code=status.HTTP_200_OK)
async def delete_short_url(user: user_dependency, short_url_id: str) -> dict:
    async with httpx.AsyncClient() as client:
        await client.delete(endpoint(f"/api/v1/short_url/{short_url_id}"))

    return {"message": f"URL with id:{short_url_id} deleted successfully."}
