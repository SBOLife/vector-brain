"""SQLAlchemy models for storing and managing text embeddings.

This module defines the database models used to store text content and their
corresponding vector embeddings using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from pgvector.sqlalchemy import Vector
from vector_brain.db.session import Base


class Embedding(Base):
    """SQLAlchemy model for storing text embeddings.

    This class represents a database table that stores text content along with its
    corresponding vector embeddings. Each embedding is a 768-dimensional vector
    representation of the text content.
    """

    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    embedding = Column(Vector(768))
