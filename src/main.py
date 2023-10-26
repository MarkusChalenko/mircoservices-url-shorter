"""Project entrypoint"""
import multiprocessing

import uvicorn
from fastapi import FastAPI

from core.config import app_settings

app = FastAPI()


@app.get("/")
def root():
    """root route"""
    return "Hello World"


if __name__ == '__main__':
    options = {
        "host": f'{app_settings.app_host}',
        "port": app_settings.app_port,
        "workers": multiprocessing.cpu_count(),
    }

    print(options)
    uvicorn.run(
        'main:app',
        **options
    )
