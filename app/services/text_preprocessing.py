import tiktoken

def chunck_text(text: str, max_tokens: int = 512) -> list[str]:
    """
    Chunk text into smaller chunks of max_tokens length.
    """
    encoding = tiktoken.encoding_for_model("cl100k_base")
    
    words = text.split()
    chunks, chunk = [], []

    for word in words:
        chunk.append(word)
        if len(encoding.encode(" ".join(chunk))) >= max_tokens:
            chunks.append(" ".join(chunk))
            chunk = []
    if chunk:
        chunks.append(" ".join(chunk))
    return chunks
    