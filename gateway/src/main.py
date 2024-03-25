import multiprocessing

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.config import app_settings
from auth.decode import decode_router

app = FastAPI(
    title="Gateway",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    redoc_url=None
)

app.include_router(decode_router, prefix="/api/v1")

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
