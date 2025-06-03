"""
FastAPI application for RAG (Retrieval Augmented Generation) microservice.
This module initializes the FastAPI application and includes routers for the API endpoints.
"""

from fastapi import FastAPI
from vector_brain.api.v1.endpoints import rag
from vector_brain.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RAG Microservice")

app.include_router(rag.router, prefix="/api/v1")
