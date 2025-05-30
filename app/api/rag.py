from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db
from app.models.vector import VectorDocument

router = APIRouter()

@router.get("/rag")
def semantic_search(query_embedding: list[float] = Query(...),
db: Session = Depends(get_db),
top_k: int = 5
):
    query = text("""
        SELECT id, content
        FROM vector_documents
        ORDER BY embedding <-> :embedding
        LIMIT :top_k
    """)
    results = db.execute(query, {"embedding": query_embedding, "top_k": top_k}).fetchall()
    return [{"id": result[0], "content": result[1]} for result in results]