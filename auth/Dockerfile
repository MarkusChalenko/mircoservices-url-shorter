FROM python:3.10-alpine3.18

ENV PYTHONPATH=src/
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add netcat-openbsd build-base libffi-dev

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.6.1 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY .env .
COPY alembic.ini .
COPY migrations ./migrations
COPY entrypoint.sh .
COPY src ./src/

VOLUME /app

ENTRYPOINT ["sh", "entrypoint.sh"]
