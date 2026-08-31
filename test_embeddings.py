from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = [
    "Hospitalization is covered under the insurance policy.",
    "The policy covers inpatient hospital treatment.",
    "Dental treatment is not covered."
]

embeddings = model.encode(sentences)

print("Embedding model loaded successfully.")
print("Number of sentences:", len(sentences))
print("Embedding shape:", embeddings.shape)