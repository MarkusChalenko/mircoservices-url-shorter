import httpx
from fastapi import APIRouter
from starlette import status
from starlette.requests import Request

from auth.auth import user_dependency
from schemas.auth_microservice.user import UserRead, UserCreate, UserUpdate

from core.config import app_settings

user_router = APIRouter(
    prefix="/user",
    tags=['auth_user_microservice']
)

auth_microservice_url: str = app_settings.auth_service_url


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(request: Request, user: user_dependency, user_id: int):
    async with httpx.AsyncClient(base_url=auth_microservice_url) as client:
        response = await client.get(f"/api/v1/user/{user_id}",
                                    headers=request.headers)
        user = response.json()

    return user


@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def create_user(create_user_data: UserCreate):
    async with httpx.AsyncClient(base_url=auth_microservice_url) as client:
        user_data_dict = create_user_data.dict()
        user_data_dict['registered_at'] = create_user_data.registered_at.isoformat()
        response = await client.post(f"/api/v1/user/", json=user_data_dict)
        user: UserRead = response.json()
    return user


@user_router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserRead)
async def update_existing_user(request: Request,
                               user: user_dependency,
                               user_id: int,
                               update_user_data: UserUpdate) -> UserRead:
    async with httpx.AsyncClient(base_url=auth_microservice_url) as client:
        response = await client.put(f"/api/v1/user/{user_id}",
                                    json=update_user_data.dict(),
                                    headers=request.headers)
        user: UserRead = response.json()
    return user


@user_router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_existing_user(request: Request,
                               user: user_dependency,
                               delete_user_id: int) -> dict:
    async with httpx.AsyncClient(base_url=auth_microservice_url) as client:
        await client.delete(f"/api/v1/user/{delete_user_id}",
                            headers=request.headers)
        return {"message": f"User with id:{delete_user_id} deleted successfully."}
