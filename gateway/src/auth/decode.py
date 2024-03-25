from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"

decode_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=e)


@decode_router.get("/secure_endpoint")
async def secure_endpoint(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    return {"token_payload": payload}