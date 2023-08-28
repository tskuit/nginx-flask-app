#!/bin/bash

GUNICORN_APP="${GUNICORN_APP:-app:app}"
GUNICORN_HOST="${GUNICORN_HOST:-127.0.0.1}"
GUNICORN_PORT="${GUNICORN_PORT:-8082}"
GUNICORN_WORKERS="${GUNICORN_WORKERS:-5}"

gunicorn \
        --bind="${GUNICORN_HOST}:${GUNICORN_PORT}" \
        --workers="${GUNICORN_WORKERS}" \
        ${GUNICORN_APP}