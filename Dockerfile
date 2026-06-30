# Stage 1: Builder stage for dependencies
FROM python:3.11-slim-bookworm AS builder

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Install build dependencies and clean up in same layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/*

ENV APP_HOME /ac_news

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --default-timeout=3000

# NGINX config
#COPY nginx.conf /etc/nginx/conf.d/acnews.conf

ADD . $APP_HOME
