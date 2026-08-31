import faiss
import numpy as np

from rag.embeddings import model


INDEX_PATH = "models/faiss_index/policy.index"

index = faiss.read_index(INDEX_PATH)


query = input("Enter your insurance question: ")


query_embedding = model.encode(
    [query],
    convert_to_numpy=True
)

query_embedding = np.asarray(
    query_embedding,
    dtype="float32"
)


distances, indices = index.search(
    query_embedding,
    3
)


print("\nTop 3 matching chunks:\n")

for i in range(3):
    print(
        f"Result {i + 1}: "
        f"Chunk index = {indices[0][i]}, "
        f"Distance = {distances[0][i]}"
    )