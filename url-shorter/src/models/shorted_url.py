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


class UpdateShortedUrl(BaseModel):
    shorted: str
    is_active: bool
    count_of_visits: int
    expire_at: datetime.datetime


class ShortedUrl(Url):
    id: str | CustomObjectId = Field(alias="_id")
    shorted: str
    is_active: bool
    user_id: int
    count_of_visits: int
    expire_at: datetime.datetime

    def convert_to_update_model(self) -> UpdateShortedUrl:
        return UpdateShortedUrl(
            shorted=self.shorted,
            is_active=self.is_active,
            count_of_visits=self.count_of_visits,
            expire_at=self.expire_at
        )


class ReadShortedUrl(ShortedUrl):
    pass
