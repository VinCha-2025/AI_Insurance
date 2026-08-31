from sentence_transformers import SentenceTransformer

print("Loading local embedding model...")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

text = """
Health insurance policies provide coverage for hospitalization expenses.
The policyholder must submit the required medical documents.
Pre-authorization may be required before certain treatments.
Some cosmetic procedures may be excluded from coverage.
Emergency hospitalization may be covered according to policy terms.
"""

# Simple chunking
chunk_size = 200

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size].strip()

    if chunk:
        chunks.append(chunk)

print("\nChunks created:")
print("-" * 50)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)

# Generate embeddings locally
embeddings = model.encode(chunks)

print("\n" + "=" * 50)
print("Embedding generation successful!")
print("Number of chunks:", len(chunks))
print("Embedding dimensions:", embeddings.shape)