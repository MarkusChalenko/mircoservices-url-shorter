import datetime
from typing import Optional

from pydantic import EmailStr, BaseModel


class UserBase(BaseModel):
    login: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    registered_at: datetime.datetime


class UserRead(UserBase):
    id: int
    registered_at: datetime.datetime


class UserUpdate(UserBase):
    login: Optional[str] = None
    email: Optional[EmailStr] = None
