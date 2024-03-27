import datetime

from bson import ObjectId
from pydantic import BaseModel, Field, ValidationError, HttpUrl


class CustomObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value, values):
        if not isinstance(value, ObjectId):
            raise ValueError('Invalid ObjectId format')
        return str(value)


class Url(BaseModel):
    origin: HttpUrl


class ShortedUrl(Url):
    id: str | CustomObjectId = Field(alias="_id")
    shorted: str
    user_id: int
    count_of_visits: int
    expire_at: datetime.datetime


class ReadShortedUrl(ShortedUrl):
    pass


class UpdateShortedUrl(BaseModel):
    shorted: str
    count_of_visits: int
    expire_at: datetime.datetime
