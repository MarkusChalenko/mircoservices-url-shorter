from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_async_session
from schemas.short_url import ShortUrlCreate
from services.short_url import url_service

router = APIRouter()


@router.get("/test")
def test():
    return "Aboba"


@router.post(
    "/create",
    response_model=ShortUrlCreate)
async def create_url(
        db: AsyncSession = Depends(get_async_session),
        origin: str = Query(
            example='http://google.com',
            max_length=450,
            min_length=1
        ),
        user=1,
) -> ShortUrlCreate:
    shorted_url = await url_service.create_short_url(
        db=db,
        origin=origin,
        user=user
    )
    return ShortUrlCreate(**shorted_url)
