from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")


async def generate_embedding(text: str) -> list[float]:
    """Generate an embedding vector for the given text using a sentence transformer model.

    Args:
        text (str): The input text to generate an embedding for.

    Returns:
        list[float]: A list of floating point numbers representing the text embedding vector.
    """
    return model.encode(text).tolist()
