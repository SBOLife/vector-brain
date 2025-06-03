"""This module provides functionality for generating text embeddings using the nomic-embed-text model.

It contains utilities for converting text into vector representations that can be used
for semantic search and other natural language processing tasks.
"""

import httpx


async def generate_embedding(text: str) -> list[float]:
    """Generate an embedding vector for the given text using the nomic-embed-text model.

    Args:
        text (str): The input text to generate embeddings for.

    Returns:
        list[float]: A list of floating point numbers representing the text embedding vector.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://ollama:11434/api/embeddings",
            json={"model": "nomic-embed-text", "prompt": text},
        )
        response.raise_for_status()
        return response.json()["embedding"]
