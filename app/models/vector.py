from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import VECTOR
from app.db.session import Base

class VectorDocument(Base):
    __tablename__ = "vector_documents"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    embedding = Column(VECTOR(1536), nullable=False)