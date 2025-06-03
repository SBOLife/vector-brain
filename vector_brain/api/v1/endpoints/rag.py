"""RAG (Retrieval-Augmented Generation) API endpoints.

This module provides FastAPI endpoints for querying the RAG system,
which combines document retrieval with text generation capabilities.
"""

from io import BytesIO
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from vector_brain.core.vector_store import query_embedding
from vector_brain.services.rag_pipeline import generate_embedding
from vector_brain.services.text_extractor import extract_text
from vector_brain.services.document_indexer import index_document
from vector_brain.core.deps import get_db


router = APIRouter()


@router.post("/rag/query")
async def rag_query(prompt: str, db: Session = Depends(get_db)):
    """Query the RAG (Retrieval-Augmented Generation) system.

    Args:
        prompt (str): The input query text to search for relevant documents
        db (Session): Database session dependency injection

    Returns:
        dict: Dictionary containing list of relevant document contents
    """
    embedding = await generate_embedding(prompt)
    results = query_embedding(db, embedding)
    return {"results": [r.content for r in results]}


@router.post("/rag/upload")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload and index a document into the RAG system.

    Args:
        file (UploadFile): The file to be uploaded and processed
        db (Session): Database session dependency injection

    Returns:
        dict: Dictionary containing success message and document ID

    Raises:
        HTTPException: If the file type is not supported
    """
    file_content = await file.read()
    text = extract_text(BytesIO(file_content), file.filename)
    if not text:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    result = await index_document(db, text)
    return {"message": "Document indexed successfully.", "id": result.id}
