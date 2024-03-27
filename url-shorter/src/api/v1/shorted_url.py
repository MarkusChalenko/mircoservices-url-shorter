from fastapi import APIRouter
from starlette import status

from auth.auth import user_dependency
from models.shorted_url import ShortedUrl, Url, UpdateShortedUrl

from services.shorted_url import get_su, create_su, update_su, delete_su, get_su_by_shorted

short_url_router = APIRouter(
    prefix="/short_url",
    tags=["short_url"]
)


@short_url_router.get("/", status_code=status.HTTP_200_OK, response_model=list[ShortedUrl])
async def get_short_urls() -> list[ShortedUrl]:
    short_url = get_su()
    return short_url


@short_url_router.get("/{shorted}", status_code=status.HTTP_200_OK)
async def get_short_url(shorted: str) -> ShortedUrl | None:
    short_url = get_su_by_shorted(shorted)
    return short_url


@short_url_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShortedUrl)
async def create_short_url(user: user_dependency, url_to_short: Url) -> ShortedUrl:
    created: ShortedUrl = create_su(url_to_short=url_to_short.origin,
                                    user_id=user["id"])
    return created


@short_url_router.put("/", status_code=status.HTTP_200_OK, response_model=ShortedUrl)
async def update_short_url(user: user_dependency, short_url_id: str, short_url: UpdateShortedUrl) -> ShortedUrl:
    return update_su(short_url_id, short_url)


@short_url_router.delete("/", status_code=status.HTTP_200_OK)
async def delete_short_url(user: user_dependency, short_url_id: str) -> dict:
    deleted: dict = delete_su(short_url_id)
    return deleted
