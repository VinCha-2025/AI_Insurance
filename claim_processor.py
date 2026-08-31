import faiss
import json
import numpy as np

from rag.embeddings import model
from decision_engine import evaluate_claim
from llm_service import generate_claim_explanation


INDEX_PATH = "models/faiss_index/policy.index"
CHUNKS_PATH = "models/faiss_index/chunks.json"


def retrieve_policy(query, top_k=3):

    index = faiss.read_index(INDEX_PATH)

    with open(
        CHUNKS_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        chunks = json.load(file)


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
        top_k
    )


    results = []


    for i in range(top_k):

        chunk_index = int(
            indices[0][i]
        )


        results.append(
            {
                "text": chunks[chunk_index],
                "distance": float(
                    distances[0][i]
                )
            }
        )


    return results


def process_claim(claim):

    # --------------------------------
    # STEP 1: Create search query
    # --------------------------------

    query = (
        claim["diagnosis"]
        + " "
        + claim["procedure"]
    )


    # --------------------------------
    # STEP 2: Retrieve policy evidence
    # --------------------------------

    policy_results = retrieve_policy(
        query
    )


    # --------------------------------
    # STEP 3: Apply decision rules
    # --------------------------------

    decision = evaluate_claim(
        claim
    )


    # --------------------------------
    # STEP 4: Ask local LLM to explain
    # --------------------------------

    explanation = generate_claim_explanation(
        claim,
        decision,
        policy_results
    )


    # --------------------------------
    # STEP 5: Return everything
    # --------------------------------

    return {

        "claim": claim,

        "decision": decision,

        "explanation": explanation,

        "policy_evidence": policy_results
    }