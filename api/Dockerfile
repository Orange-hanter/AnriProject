FROM python:3.11.4-slim as base

ARG DOCKER_USER_ID=1000
ARG DOCKER_GROUP_ID=1000

ENV PYTHONUNBUFFERED 1

RUN groupadd -g ${DOCKER_GROUP_ID} user \
    && useradd --shell /bin/bash -u $DOCKER_USER_ID -g $DOCKER_GROUP_ID -o -c "" -m user

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential \
    python3-dev \
    libpq-dev \
    tzdata \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

RUN pip install --no-cache -U pip setuptools poetry==1.4.0 \
    && rm -rf /root/.cache/pip

COPY --chown=user:user ./pyproject.toml ./poetry.lock /opt/api/

WORKDIR /opt/api/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-cache --no-ansi --no-interaction --only main \
    && poetry cache clear pypi --all

COPY --chown=user:user ./docker-entrypoint.sh ./wait-for-dependencies.py /opt/api/

RUN mkdir -p /opt/api/synapsis/public/media/ \
    && mkdir -p /opt/api/synapsis/public/static/ \
    && chown user:user -R /opt/api/synapsis/public/

ENTRYPOINT ["/opt/api/docker-entrypoint.sh"]



FROM base as local

RUN poetry install --no-root --no-cache --no-ansi --no-interaction --with dev \
    && poetry cache clear pypi --all

USER user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



FROM base as live

COPY --chown=user:user . /opt/api

USER user

EXPOSE 8000

CMD ["gunicorn", "synapsis.wsgi:application", "--bind", "0.0.0.0", "--worker-tmp-dir", "/dev/shm", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-"]
