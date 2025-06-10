"""RAG (Retrieval Augmented Generation) endpoints for document processing and querying.

This module provides FastAPI endpoints for:
- Querying the vector store using RAG
- Uploading and indexing documents
"""

from io import BytesIO
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from vector_brain_backend.core.vector_store import query_embedding
from vector_brain_backend.services.rag_pipeline import generate_embedding
from vector_brain_backend.services.text_extractor import extract_text
from vector_brain_backend.services.document_indexer import index_document
from vector_brain_backend.schemas.rag import QueryRequest
from vector_brain_backend.core.deps import get_db

router = APIRouter()


@router.post("/rag/query")
async def rag_query(request: QueryRequest, db: Session = Depends(get_db)):
    """Query the vector store using RAG (Retrieval Augmented Generation).

    Args:
        request (QueryRequest): The query request containing the prompt
        db (Session): Database session dependency

    Returns:
        dict: A dictionary containing the query results with matching content
    """

    embedding = await generate_embedding(request.prompt)
    results = query_embedding(db, embedding)
    return {"results": [r.content for r in results]}


@router.post("/rag/upload")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload and index a document file.

    Args:
        file (UploadFile): The file to be uploaded and processed
        db (Session): Database session dependency

    Returns:
        dict: A dictionary containing success message and document ID

    Raises:
        HTTPException: If the file type is not supported
    """

    file_content = await file.read()
    text = extract_text(BytesIO(file_content), file.filename)
    if not text:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    result = await index_document(db, text)
    return {"message": "Document indexed successfully.", "id": result.id}
