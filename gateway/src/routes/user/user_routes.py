import httpx
from fastapi import APIRouter
from starlette import status

from auth.auth import user_dependency
from schemas.auth_microservice.user import UserRead, UserCreate, UserUpdate

from core.config import app_settings

user_router = APIRouter(
    prefix="/user",
    tags=['auth_user_microservice']
)

auth_microservice_url: str = app_settings.auth_service_url


def endpoint(endp: str) -> str:
    return auth_microservice_url + endp


@user_router.get("/secure_endpoint", status_code=status.HTTP_200_OK)
async def secure_endpoint(user: user_dependency):
    return {"resp": "123"}


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, user_id: int):
    print("/user_router.get")
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint(f"/api/v1/user/{user_id}"))
        user = response.json()

    return user


@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def create_user(create_user_data: UserCreate):
    async with httpx.AsyncClient() as client:
        user_data_dict = create_user_data.dict()
        user_data_dict['registered_at'] = create_user_data.registered_at.isoformat()
        response = await client.post(endpoint(f"/api/v1/user/"), json=user_data_dict)
        user: UserRead = response.json()
    return user


@user_router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserRead)
async def update_existing_user(user_id: int,
                               update_user_data: UserUpdate) -> UserRead:
    async with httpx.AsyncClient() as client:
        response = await client.put(endpoint(f"/api/v1/user/{user_id}"), json=update_user_data.dict())
        user: UserRead = response.json()
    return user


@user_router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_existing_user(delete_user_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        await client.delete(endpoint(f"/api/v1/user/{delete_user_id}"))
        return {"message": f"User with id:{delete_user_id} deleted successfully."}



