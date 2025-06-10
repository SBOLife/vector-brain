#!/bin/bash

check_ollama_ready() {
    if wget -q -S -O - http://ollama:11434 2>&1 | grep -q "HTTP/.* 200"; then
        return 0
    else
        return 1
    fi
}


echo "Waiting for PostgreSQL..."
until pg_isready -h db -U postgres >/dev/null 2>&1; do
    sleep 1
done
echo "PostgreSQL is ready!"

echo "Waiting for Ollama to be fully ready..."
attempt=1
max_attempts=30

while ! check_ollama_ready; do
    if [ $attempt -ge $max_attempts ]; then
        echo "Ollama failed to start after $max_attempts attempts"
        exit 1
    fi
    
    echo "Attempt $attempt/$max_attempts - Ollama not fully ready yet..."
    sleep 5
    ((attempt++))
done

echo "Ollama is fully ready and running!"

alembic upgrade head

exec streamlit run vector_brain_frontend/app.py &
exec uvicorn vector_brain_backend.main:app --host 0.0.0.0 --port 8000