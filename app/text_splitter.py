def split_text(text, chunk_size=500, overlap=100):
    """
    Split text into smaller chunks with overlapping content.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        # Try to avoid cutting a word in half.
        if end < len(text):
            last_space = text.rfind(" ", start, end)
            if last_space > start:
                end = last_space

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(text):
            break

        start = end - overlap

    return chunks


def create_chunks(documents, chunk_size=500, overlap=100):
    """
    Split extracted PDF pages while preserving their metadata.
    """

    all_chunks = []

    for document in documents:
        text = document["content"]
        metadata = document["metadata"]

        text_chunks = split_text(text, chunk_size, overlap)

        for index, chunk in enumerate(text_chunks):
            all_chunks.append({
                "content": chunk,
                "metadata": {
                    **metadata,
                    "chunk": index + 1
                }
            })

    return all_chunks