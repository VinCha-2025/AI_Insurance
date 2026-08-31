import faiss
import json
import numpy as np

from rag.embeddings import model


INDEX_PATH = "models/faiss_index/policy.index"
CHUNKS_PATH = "models/faiss_index/chunks.json"


# Load FAISS index
index = faiss.read_index(INDEX_PATH)


# Load original chunks
with open(CHUNKS_PATH, "r", encoding="utf-8") as file:
    chunks = json.load(file)


# Get user question
query = input("Enter your insurance question: ")


# Convert question into embedding
query_embedding = model.encode(
    [query],
    convert_to_numpy=True
)

query_embedding = np.asarray(
    query_embedding,
    dtype="float32"
)


# Search top 3 results
distances, indices = index.search(
    query_embedding,
    3
)


print("\n================================")
print("RELEVANT POLICY INFORMATION")
print("================================")


for i in range(3):

    chunk_index = indices[0][i]

    print(f"\nResult {i + 1}")
    print("-----------------------------")

    print(chunks[chunk_index])

    print(
        f"\nSimilarity distance: "
        f"{distances[0][i]:.4f}"
    )