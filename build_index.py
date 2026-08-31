import faiss
import json
import os

from rag.pdf_loader import load_pdf
from rag.chunking import create_chunks
from rag.embeddings import create_embeddings
from rag.vector_store import create_faiss_index


PDF_PATH = "data/policies/health_policy.pdf"

INDEX_PATH = "models/faiss_index/policy.index"
CHUNKS_PATH = "models/faiss_index/chunks.json"


print("Loading PDF...")

text = load_pdf(PDF_PATH)


print("Creating chunks...")

chunks = create_chunks(
    text,
    chunk_size=100
)

print("Number of chunks:", len(chunks))


print("Creating embeddings...")

embeddings = create_embeddings(chunks)

print("Embedding shape:", embeddings.shape)


print("Creating FAISS index...")

index = create_faiss_index(embeddings)


# Create folder if it doesn't exist
os.makedirs("models/faiss_index", exist_ok=True)


print("Saving FAISS index...")

faiss.write_index(
    index,
    INDEX_PATH
)


print("Saving chunks...")

with open(CHUNKS_PATH, "w", encoding="utf-8") as file:
    json.dump(
        chunks,
        file,
        ensure_ascii=False,
        indent=2
    )


print("\n================================")
print("INDEX BUILDING COMPLETE")
print("================================")

print("FAISS index:", INDEX_PATH)
print("Chunks:", CHUNKS_PATH)