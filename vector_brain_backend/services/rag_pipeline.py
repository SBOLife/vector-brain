"""This module provides functionality for generating text embeddings using sentence transformers.

It contains utilities for caching and generating embeddings from text input using the
'all-mpnet-base-v2' model. The embeddings can be used for semantic text operations like
similarity matching and retrieval.
"""

from sentence_transformers import SentenceTransformer


async def generate_embedding(text: str) -> list[float]:
    """Generate embeddings for the given text using a sentence transformer model.

    Args:
        text (str): The input text to generate embeddings for.

    Returns:
        list[float]: A list of floating point numbers representing the text embedding vector.
    """
    model = SentenceTransformer("all-mpnet-base-v2")
    return model.encode(text).tolist()
