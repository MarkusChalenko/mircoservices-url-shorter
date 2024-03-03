from pydantic import BaseModel, HttpUrl


class ShortUrlBase(BaseModel):
    origin_url: HttpUrl
    shorted_url: HttpUrl

    class Config:
        orm_model = True


class ShortUrlCreate(ShortUrlBase):
    pass


class ShortUrlRead(ShortUrlBase):
    is_active: bool


class ShortUrlDelete(ShortUrlBase):
    is_active: bool
