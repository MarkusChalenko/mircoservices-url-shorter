import multiprocessing

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

from core.config import app_settings
from routes import api_router

app = FastAPI(
    title="Gateway",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


app.include_router(api_router)

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
