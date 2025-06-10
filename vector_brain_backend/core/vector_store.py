"""Database operations for storing and querying vector embeddings.

This module provides functions to interact with a vector database, allowing storage
and similarity-based retrieval of text embeddings using SQLAlchemy ORM.
"""

from sqlalchemy.orm import Session
from vector_brain_backend.models.embeddings import Embedding


def add_embedding(
    db: Session, content: str, embedding_vector: list[float]
) -> Embedding:
    """Add a new text embedding to the database.

    Args:
        db (Session): SQLAlchemy database session
        content (str): The text content to be stored
        embedding_vector (list[float]): Vector representation of the content

    Returns:
        Embedding: The newly created embedding object
    """
    embedding = Embedding(content=content, embedding=embedding_vector)
    db.add(embedding)
    db.commit()
    db.refresh(embedding)
    return embedding


def query_embedding(
    db: Session, embedding_vector: list[float], top_k: int = 5
) -> list[Embedding]:
    """Query the database for embeddings similar to the given vector.

    Args:
        db (Session): SQLAlchemy database session
        embedding_vector (list[float]): Vector to compare against stored embeddings
        top_k (int, optional): Number of most similar embeddings to return. Defaults to 5.

    Returns:
        list[Embedding]: List of most similar embeddings, ordered by L2 distance
    """
    return (
        db.query(Embedding)
        .order_by(Embedding.embedding.l2_distance(embedding_vector))
        .limit(top_k)
        .all()
    )
