"""Database configuration module.

This module handles database connection configuration using SQLAlchemy.
It sets up the database URL, engine, session factory and declarative base.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from vector_brain_backend.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
