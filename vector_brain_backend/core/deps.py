"""Database dependency module for FastAPI endpoints.

This module provides database session dependency injection for FastAPI routes.
"""

from vector_brain_backend.db.session import SessionLocal


def get_db():
    """Get a database session.

    Yields:
        SessionLocal: A SQLAlchemy database session that will be automatically closed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
