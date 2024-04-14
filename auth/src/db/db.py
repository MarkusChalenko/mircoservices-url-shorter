from typing import Union, Callable, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (async_sessionmaker,
                                    create_async_engine,
                                    AsyncSession, AsyncEngine, AsyncConnection)

from core.config import app_settings


async def get_async_session() -> AsyncSession:
    """
        Returns an asynchronous session using the `async_session` context manager.

        This function establishes an asynchronous session using the `async_session` context manager,
        which creates and manages an execution context for asynchronous operations.

        if ERROR - rollback and close.
        :return: AsyncSession
    """
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()


def create_sessionmaker(
        bind_engine: Union[AsyncEngine, AsyncConnection]
) -> Callable[..., async_sessionmaker]:
    """
        Creates and returns an asynchronous session maker.

        :param bind_engine: Union[AsyncEngine, AsyncConnection]
        :return: Callable[..., async_sessionmaker]
    """
    return async_sessionmaker(
        bind=bind_engine,
        expire_on_commit=False,
        future=True,
        class_=AsyncSession,
        autoflush=False
    )


engine = create_async_engine(app_settings.postgres_dsn.unicode_string())
async_session = create_sessionmaker(engine)
db_dependency = Annotated[AsyncSession, Depends(get_async_session)]