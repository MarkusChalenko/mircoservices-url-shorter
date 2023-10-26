FROM python:3.10-alpine3.18

RUN apk update && \
    apk add netcat-openbsd build-base libffi-dev

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.6.1 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}


COPY .env .
COPY src ./src/

#CMD while ! nc -z $DB_HOST $DB_PORT; do \
#      sleep 0.1; \
#    done && \
#    alembic upgrade head

ENTRYPOINT ["python3", "src/main.py"]