from fastapi_users.schemas import BaseUserCreate, BaseUser


class UserRead(BaseUser[int]):
    id: int
    email: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_model = True


class UserCreate(BaseUserCreate):
    username: str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
