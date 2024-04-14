from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean

from schemas.user import UserRead
from .base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    login = Column(String, nullable=False, unique=True, index=True)
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)

    def to_user_read(self) -> UserRead:
        return UserRead(
            id=self.id,
            login=self.login,
            email=self.email,
            registered_at=self.registered_at,
        )
