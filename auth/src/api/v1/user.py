from fastapi import APIRouter
from starlette import status

from db.db import db_dependency
from schemas.user import UserCreate, UserRead, UserUpdate
from services.user import create_new_user, get_user_by_id, update_user, delete_user

from services.auth import user_dependency

user_router = APIRouter(
    prefix="/user",
    tags=['user']
)


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserRead)
async def get_user(db: db_dependency,
                   user_id: int):
    user: UserRead = await get_user_by_id(db=db, user_id=user_id)
    return user


@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def create_user(db: db_dependency,
                      create_user_data: UserCreate):
    created_user: UserRead = await create_new_user(db=db, user_data=create_user_data)
    return created_user


@user_router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserRead)
async def update_existing_user(user: user_dependency,
                               db: db_dependency,
                               user_id: int,
                               update_user_data: UserUpdate) -> UserRead:
    updated_user_data: UserRead = \
        await update_user(db=db, user_id=user_id, update_data=update_user_data)
    return updated_user_data


@user_router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_existing_user(user: user_dependency,
                               db: db_dependency,
                               delete_user_id: int):
    await delete_user(db=db, user_id=delete_user_id)
    return {"message": f"User with id:{delete_user_id} deleted successfully."}
