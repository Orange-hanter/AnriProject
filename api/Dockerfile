FROM python:3.11.5-slim

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

RUN pip install --upgrade pip

RUN pip install --no-cache -U pip setuptools poetry==1.5.1 \
    && rm -rf /root/.cache/pip

WORKDIR /opt/api/

COPY pyproject.toml .

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-cache --no-ansi --no-interaction\
    && poetry cache clear pypi --all

COPY . .

RUN chmod a+x ./scripts/start-dev.sh

ENTRYPOINT ./scripts/start-dev.sh
