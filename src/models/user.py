from sqlalchemy import Column, Integer, String

from .base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)
