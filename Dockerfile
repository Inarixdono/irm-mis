# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13.0
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

RUN mkdir -p /app/.pytest_cache && chmod -R 777 /app/.pytest_cache

USER appuser

COPY . .

EXPOSE 8000

CMD uvicorn 'app:app' --host=0.0.0.0 --port=8000
