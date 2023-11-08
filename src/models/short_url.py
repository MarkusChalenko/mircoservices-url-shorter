from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from .base import Base


class ShortUrl(Base):
    __tablename__ = "short_url"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    origin_url = Column(String, unique=True)
    shorted_url = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
