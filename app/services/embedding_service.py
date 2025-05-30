from typing import List
import hashlib
import httpx
import numpy as np
from app.core.config import OLLAMA_API_BASE_URL

EMBED_CACHE = {}


def generate_embedding(text: str, model: str) -> List[float]:
    """
    Generate an embedding for a given text using a specified model.
    """
    key = hashlib.sha256(text.encode()).hexdigest()
    if key in EMBED_CACHE:
        return EMBED_CACHE[key]

    response = httpx.post(
        OLLAMA_API_BASE_URL,
        json={
            "model": model,
            "prompt": text,
        },
    )

    response.raise_for_status()
    embedding = response.json()["embedding"]
    EMBED_CACHE[key] = embedding
    return embedding


def normalize_embedding(embedding: List[float]) -> List[float]:
    """
    Normalize an embedding to have a unit norm.
    """
    vector = np.array(embedding)
    normalized_vector = np.linalg.norm(vector)
    return (
        (vector / normalized_vector).tolist() if normalized_vector != 0 else embedding
    )
