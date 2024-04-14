import multiprocessing

import httpx
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from auth.auth import user_dependency
from core.config import app_settings
from routes.token.token import token_router
from routes.user.user_routes import user_router
from routes.url_shorter.url_shorter_routes import url_shorter_router

app = FastAPI(
    title="Gateway",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    redoc_url=None
)


app.include_router(user_router, prefix="/api/v1")
app.include_router(token_router, prefix="/api/v1")
app.include_router(url_shorter_router, prefix="/api/v1")


@app.get("/")
async def asd():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/todos/1')
        res = response.json()
    return res


@app.get("/ping_auth")
async def asd():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://auth:8001/ping')
        res = response.json()
    return res


@app.get("/ping_shorter")
async def asd(user: user_dependency):
    async with httpx.AsyncClient() as client:
        response = await client.get('http://url-shorter:8002/ping')
        res = response.json()
    return res


if __name__ == '__main__':
    options = {
        "host": f'{app_settings.app_host}',
        "port": app_settings.app_port,
        "workers": multiprocessing.cpu_count(),
        "reload": app_settings.debug,
    }

    print(options)
    uvicorn.run(
        'main:app',
        **options
    )
