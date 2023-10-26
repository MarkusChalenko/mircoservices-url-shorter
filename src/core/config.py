from pydantic.v1 import BaseSettings


class AppSettings(BaseSettings):
    app_port: int = 8000
    app_host: str = 'app'


app_settings = AppSettings()
