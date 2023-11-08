from sqlalchemy import Column, Integer, String, ForeignKey

from .base import Base


class ShortUrlStatistic(Base):
    __tablename__ = 'short_url_statistic'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    follow_count = Column(Integer, default=0)
    last_ip_follow = Column(String, nullable=True)
    url_id = Column(Integer, ForeignKey('short_url.id', ondelete='CASCADE'), nullable=False)
