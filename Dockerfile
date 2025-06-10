FROM python:3.11-bullseye AS base

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    libffi-dev \
    postgresql-client \
    curl && \
    rm -rf /var/lib/apt/lists/*

COPY ./vector_brain_backend /app/vector_brain_backend
COPY ./vector_brain_frontend /app/vector_brain_frontend
COPY ./alembic /app/alembic
COPY ./alembic.ini /app/
COPY ./entrypoint.sh /app/
COPY ./models/sentence-transformers/all-mpnet-base-v2.tar.gz /root/.cache/torch/sentence_transformers/

RUN mkdir -p /root/.cache/torch/sentence_transformers && \
    tar -xzf /root/.cache/torch/sentence_transformers/all-mpnet-base-v2.tar.gz -C /root/.cache/torch/sentence_transformers/ && \
    mv /root/.cache/torch/sentence_transformers/all-mpnet-base-v2 /root/.cache/torch/sentence_transformers/sentence-transformers_all-mpnet-base-v2 && \
    rm /root/.cache/torch/sentence_transformers/all-mpnet-base-v2.tar.gz
COPY pyproject.toml poetry.lock README.md /app/

RUN chmod +x /app/entrypoint.sh

RUN pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --only main

RUN pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir streamlit langchain langchain-community sentence-transformers

WORKDIR /app

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
