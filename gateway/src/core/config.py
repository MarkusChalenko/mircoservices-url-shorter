""" Module containing the AppSettings class that represents
the application's configuration settings."""
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    Class representing the application's configuration settings and variables.

    Attributes:
        app_port (int): The port on which the application will run. Default value: 8000.
        app_host (str): The host or IP address of the application. Default value: 'app'.
        debug (bool): Flag indicating debug application mod.
    """

    app_port: int = 8000
    app_host: str = 'app'
    debug: bool = True
    jwt_secret: str = 'SECRET'
    algorithm: str = 'HS256'
    auth_service_url: str = 'http://auth:8001'
    url_shorter_service_url: str = 'http://url-shorter:8002'

    class Config:
        _env_file = ".env"
        _extra = 'allow'


app_settings = AppSettings()
