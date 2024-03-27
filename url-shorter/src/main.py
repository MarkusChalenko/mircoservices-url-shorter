import multiprocessing

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.shorted_url import short_url_router
from api.v1.token import token_router
from core.config import app_settings
from pymongo.mongo_client import MongoClient

app = FastAPI(
    title="Url-shorter",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    redoc_url=None
)

app.include_router(short_url_router, prefix="/api/v1")
app.include_router(token_router, prefix="/api/v1")

@app.get("/")
def ping():
    uri = "mongodb://root:example@mongo:27017"
    client = MongoClient(uri)
    try:
        client.admin.command("ping")
        print("pinged")
    except Exception as e:
        print(e)


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
