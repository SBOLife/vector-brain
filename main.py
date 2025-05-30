"""
FastAPI application for Vector Brain RAG System.
This module initializes the FastAPI application and includes routers for vector operations
and RAG (Retrieval Augmented Generation) functionality.
"""

from fastapi import FastAPI
from app.api import vector, rag

app = FastAPI(title="Vector Brain - RAG System", version="1.0.0")

app.include_router(prefix="/api/v1", router=vector.router)
app.include_router(prefix="/api/v1", router=rag.router)
