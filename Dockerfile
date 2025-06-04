FROM python:3.11-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libopenblas-dev \
        liblapack-dev \
        libffi-dev \
        curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install poetry

COPY pyproject.toml README.md /app/
COPY ./vector_brain /app/vector_brain
COPY ./streamlit_chat /app/streamlit_chat
COPY ./alembic /app/alembic
COPY ./alembic.ini /app/
COPY ./entrypoint.sh /app/

RUN poetry config virtualenvs.create false && \
    poetry install --only main

# Instala torch com wheels pré-compilados
RUN pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir streamlit langchain langchain-community sentence-transformers

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
