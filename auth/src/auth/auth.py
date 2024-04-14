from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from core.config import app_settings

JWT_SECRET = app_settings.jwt_secret
ALGORITHM = app_settings.algorithm

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='v1/auth/token')
