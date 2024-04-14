from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from core.config import app_settings

SECRET_KEY = app_settings.jwt_secret
ALGORITHM = app_settings.algorithm

token_url: str = f"{app_settings.auth_service_url}/api/v1/auth/token"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    print("get_current_user HAFGAGAGA")
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        print("IN FUCKING AUTH")
        print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        username: str = payload.get("sub")
        print(username)
        if username is None:
            print("ASDADASDADA")
            raise credentials_exception
        return payload
    except JWTError:
        print("FUUUUUUUUCK")
        raise credentials_exception


user_dependency = Annotated[dict, Depends(get_current_user)]
