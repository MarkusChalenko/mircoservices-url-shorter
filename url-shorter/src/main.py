import multiprocessing
from contextlib import asynccontextmanager

import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from api.v1.shorted_url import short_url_router
from api.v1.token import token_router
from auth.auth import user_dependency
from core.config import app_settings

from schedule_tasks.deactivate_expired_urls import deactivate_expiring_urls
from services.shorted_url import get_su_by_shorted


@asynccontextmanager
async def lifespan(_: FastAPI):
    scheduler = BackgroundScheduler()
    scheduler.add_job(id="expiring_links",
                      func=deactivate_expiring_urls,
                      trigger="cron",
                      minute=30)
    scheduler.start()
    yield
    scheduler.shutdown(wait=False)

app = FastAPI(
    title="Url-shorter",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    redoc_url=None,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(short_url_router, prefix="/api/v1")
app.include_router(token_router, prefix="/api/v1")


@app.get("/ping")
async def root(user: user_dependency) -> str:
    """root route"""
    return "pong"


@app.get("/{url_hash}", response_class=RedirectResponse, tags=['redirect'])
async def redirect_to_origin(url_hash: str) -> RedirectResponse:
    short_url = get_su_by_shorted(url_hash)
    if short_url:
        return RedirectResponse(short_url.origin)
    else:
        raise HTTPException(status_code=404, detail="URL not found")


if __name__ == '__main__':
    options = {
        "host": f'{app_settings.app_host}',
        "port": app_settings.app_port,
        "workers": multiprocessing.cpu_count(),
        "reload": app_settings.debug
    }

    print(options)
    uvicorn.run(
        'main:app',
        **options
    )
