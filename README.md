# VectorBrain - RAG System Documentation

## Overview

VectorBrain is a Retrieval-Augmented Generation (RAG) system that combines document retrieval with text generation capabilities. It provides both a FastAPI backend for API access and a Streamlit chat interface for interactive use.

![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)

## Key Features

- **Document Processing**:
  - Supports PDF, DOCX, and TXT file formats
  - Automatic text extraction and vector embedding generation
  - Semantic search capabilities

- **AI Integration**:
  - Local LLM integration via Ollama
  - LangChain-powered RAG pipeline
  - Customizable prompt templates

- **Technical Infrastructure**:
  - PostgreSQL with pgvector for vector storage
  - Dockerized deployment
  - FastAPI backend with REST endpoints
  - Streamlit frontend for chat interface

## System Architecture

```mermaid
graph TD
    A[Streamlit UI] -->|HTTP| B[FastAPI]
    B --> C[PostgreSQL + pgvector]
    B --> D[Ollama LLM]
    C --> E[Document Storage]
    D --> F[Response Generation]
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

## Installation

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- Ollama installed (for local LLM)

### Quick Start with Docker

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
   streamlit run vector_brain_frontend/app.py
   ```

## Configuration

Create `.env` file:

```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/rag_db
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

## Support

For issues or questions, please open an issue in the GitHub repository.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.