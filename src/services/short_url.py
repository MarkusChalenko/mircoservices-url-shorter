from pydantic import BaseModel

from models import ShortUrl
from repositories.short_url import ShortUrlRepository


class RepositoryShortUrl(ShortUrlRepository[ShortUrl, BaseModel]):
    pass


url_service = RepositoryShortUrl(ShortUrl)
