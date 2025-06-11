# VectorBrain - RAG System with FastAPI and Streamlit

![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)

VectorBrain is a Retrieval-Augmented Generation (RAG) system that combines document retrieval with text generation capabilities, providing both a FastAPI backend and Streamlit chat interface.

## Features

- 📄 Document ingestion (PDF, DOCX, TXT)
- 🔍 Semantic search using vector embeddings
- 🤖 Local LLM integration via Ollama
- 🚀 REST API and chat interface
- 🐳 Dockerized deployment
- 🧠 LangChain-powered RAG pipeline

## System Architecture

```mermaid
graph TD
    A[Streamlit UI] -->|HTTP| B[FastAPI]
    B --> C[PostgreSQL + pgvector]
    B --> D[Ollama LLM]
    C --> E[Document Storage]
    D --> F[Response Generation]
```

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- Ollama installed (for local LLM)

### Running with Docker

```bash
docker-compose up -d
```

Services will be available at:
- FastAPI: http://localhost:8000
- Streamlit Chat: http://localhost:8501

## API Documentation

### Base URL
`http://localhost:8000`

### Endpoints

#### Query RAG System
`POST /api/v1/rag/query`

```bash
curl -X POST "http://localhost:8000/api/v1/rag/query" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"What is retrieval augmented generation?"}'
```

#### Upload Document
`POST /api/v1/rag/upload`

```bash
curl -X POST "http://localhost:8000/api/v1/rag/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.pdf"
```

## Development Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Set up pre-commit hooks:
   ```bash
   pre-commit install
   ```
4. Start dependencies:
   ```bash
   docker-compose up db ollama -d
   ```
5. Run services:
   ```bash
   # FastAPI
   uvicorn vector_brain_backend.main:app --reload
   
   # Streamlit
   streamlit run streamlit_chat/app.py
   ```

## Configuration

Create `.env` file:

```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/rag_db
```

## Database Schema

The system uses PostgreSQL with pgvector extension to store:

```mermaid
erDiagram
    EMBEDDINGS {
        int id PK
        text content
        vector(768) embedding
    }
```

## Services Overview

- **Document Indexer**: Handles document ingestion and embedding
- **RAG Pipeline**: Manages retrieval and generation
- **Text Extractor**: Processes PDF, DOCX, TXT files
- **LangChain Pipeline**: Combines retrieval with LLM generation

## Testing

```bash
pytest --cov=vector_brain
```

## License

Apache License 2.0

