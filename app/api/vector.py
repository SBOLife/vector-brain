from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.vector import VectorDocument
from app.schemas.vector import VectorCreate, VectorRead

router = APIRouter()

@router.post("/", response_model=VectorRead)
def create_vector(vector: VectorCreate, db: Session = Depends(get_db)):
    db_vector = VectorDocument(
        content=vector.content,
        embedding=vector.embedding
    )
    db.add(db_vector)
    db.commit()
    db.refresh(db_vector)
    return db_vector