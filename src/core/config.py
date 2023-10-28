"""Configs of whole project"""
from pydantic.v1 import BaseSettings


class AppSettings(BaseSettings):
    """Configs of whole project"""
    app_port: int = 8000
    app_host: str = 'app'


app_settings = AppSettings()
