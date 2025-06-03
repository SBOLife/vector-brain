FROM python:3.11-slim

WORKDIR /app

RUN pip install -e .

COPY ./vector_brain /app/vector_brain

CMD ["uvicorn", "vector_brain.main:app", "--host", "0.0.0.0", "--port", "8000"]
