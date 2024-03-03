import hashlib
from typing import Generic, TypeVar, Type

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from models import ShortUrl

ShortUrlModel = TypeVar('ShortUrlModel', bound=ShortUrl)
ShortUrlSchema = TypeVar('ShortUrlSchema', bound=BaseModel)


class ShortUrlRepository(Generic[ShortUrlModel, ShortUrlSchema]):
    def __init__(self, short_url: Type[ShortUrlModel]):
        self._short_url = short_url

    async def create_short_url(self, db: AsyncSession, origin: str, user: int) -> ShortUrlModel:
        short_url = self._short_url(
            origin=origin,
            shorted=hashlib.sha256(bytes(origin, 'utf-8')),
            user=user
        )
        db.add(short_url)
        try:
            await db.commit()
            await db.refresh(short_url)
        except exc.SQLAlchemyError as error:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail=error
            )
        return short_url
