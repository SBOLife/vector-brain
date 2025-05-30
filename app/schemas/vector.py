"""Vector schema models for the application.

This module defines Pydantic models for vector operations, including creation
and retrieval of vectors with their associated content and embeddings.
"""

from typing import List
from pydantic import BaseModel


class VectorCreate(BaseModel):
    """Pydantic model for creating a vector.

    Represents the schema for creating a new vector with content and embedding data.
    """

    content: str
    embedding: List[float]


class VectorRead(VectorCreate):
    """Pydantic model for reading a vector.

    Extends VectorCreate to include an ID field for retrieving existing vectors.
    """

    id: int
