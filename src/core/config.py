""" Module containing the AppSettings class that represents
the application's configuration settings."""
from pydantic import PostgresDsn
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    Class representing the application's configuration settings and variables.

    Attributes:
        app_port (int): The port on which the application will run. Default value: 8000.
        app_host (str): The host or IP address of the application. Default value: 'app'.
        postgres_dsn (PostgresDsn): The DSN (Data Source Name) for the Postgres database.
        redis_host (str): The host or IP address of the Redis cache. Default value: 'cache'.
        redis_port (int): The port on which the Redis cache is running. Default value: 6379.
        postgres_echo (bool): Flag indicating whether database queries should be echoed.
    """

    app_port: int = 8000
    app_host: str = 'app'
    postgres_dsn: PostgresDsn = MultiHostUrl(
        'postgresql+asyncpg://postgres:postgres@database:5432/postgres')
    redis_host: str = 'cache'
    redis_port: int = 6379
    postgres_echo: bool = False

    class Config:
        _env_file = ".env"
        _extra = 'allow'


app_settings = AppSettings()
