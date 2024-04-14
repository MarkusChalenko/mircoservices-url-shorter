FROM python:3.11-alpine3.18

ENV PYTHONPATH=src/
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add build-base libffi-dev

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.6.1 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY .env .
COPY src ./src/
COPY entrypoint.sh .

VOLUME /app

ENTRYPOINT ["python3", "src/main.py"]
