from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from db.db import db_dependency
from schemas.token import Token
from services.auth import authenticate_user, create_access_token, user_dependency

auth_router = APIRouter(
    prefix="/auth",
    tags=['auth']
)


@auth_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate user.")
    token = create_access_token(user.login, user.id, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}


@auth_router.get("/login")
def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Not Authenticated")
    return {"user": user}


