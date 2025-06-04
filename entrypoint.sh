#!/bin/bash
set -e

echo "✅ Wainting DB to start..."
until pg_isready -h db -U postgres; do
  sleep 1
done

echo "✅ Database is ready."

echo "✅ Migrations running..."
alembic upgrade head

echo "✅ Starting FastAPI..."
uvicorn vector_brain.main:app --host 0.0.0.0 --port 8000 &

echo "✅ Starting Streamlit..."
streamlit run /app/streamlit_chat/app.py --server.port 8501 --server.address 0.0.0.0
