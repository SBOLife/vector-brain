from pydantic import BaseModel
from typing import List

class VectorCreate(BaseModel):
    content: str
    embedding: str

class VectorRead(VectorCreate):
    id: int