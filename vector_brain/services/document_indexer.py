"""
Document indexing service module.

This module provides functionality for indexing documents by generating
and storing their embedding vectors in a vector store database.
"""

from sqlalchemy.orm import Session
from vector_brain.services.rag_pipeline import generate_embedding
from vector_brain.core.vector_store import add_embedding


async def index_document(db: Session, content: str):
    """Index a document by generating and storing its embedding vector.

    Args:
        db (Session): SQLAlchemy database session
        content (str): Text content to be indexed

    Returns:
        The stored embedding record from the vector store
    """
    embedding = await generate_embedding(content)
    return add_embedding(db, content, embedding)
