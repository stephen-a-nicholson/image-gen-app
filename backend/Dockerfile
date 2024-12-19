FROM python:3.12-slim-bookworm

WORKDIR /app/

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

ENV PYTHONPATH=/app

COPY ./simple_webapp_k8s /app/simple_webapp_k8s

EXPOSE 8000

CMD ["gunicorn", "--timeout", "600", "--workers", "4", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "simple_webapp_k8s.api:app"]