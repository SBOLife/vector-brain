"""
This module defines Pydantic models for RAG (Retrieval-Augmented Generation) related schemas.
These schemas are used to validate and structure data for RAG operations in the vector brain backend.
"""

from pydantic import BaseModel


class QueryRequest(BaseModel):
    """A model representing a query request.

    This class defines the structure for query requests, containing a prompt string
    that will be used for retrieving relevant information.
    """

    prompt: str
