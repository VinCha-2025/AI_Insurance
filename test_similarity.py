from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Hospitalization expenses are covered by the insurance policy.",
    "The policy provides coverage for inpatient hospital treatment.",
    "Dental cosmetic procedures are excluded from coverage.",
    "The policy covers emergency medical treatment."
]

query = "Does the insurance cover hospital admission?"

document_embeddings = model.encode(documents)
query_embedding = model.encode([query])

similarities = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

for i, score in enumerate(similarities):
    print(f"{score:.4f} - {documents[i]}")