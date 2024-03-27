from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from starlette import status

from auth.auth import token_url

token_router = APIRouter(
    prefix="/token",
    tags=["token"]
)


class Token(BaseModel):
    access_token: str
    token_type: str


@token_router.post("/", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    async with httpx.AsyncClient() as client:
        data = {
            "grant_type": form_data.grant_type,
            "username": form_data.username,
            "password": form_data.password,
            "client_id": form_data.client_id,
            "client_secret": form_data.client_secret
        }

        response = await client.post(url=token_url, data=data)

        if not response:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user.")

        token: Token = response.json()

        return token
