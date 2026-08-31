from llm_service import generate_claim_explanation


claim = {
    "age": 45,
    "diagnosis": "Appendicitis",
    "procedure": "Appendectomy",
    "claim_amount": 80000
}


decision = {
    "decision": "APPROVED",
    "reason": (
        "The requested surgical procedure "
        "is listed as covered."
    )
}


policy_evidence = [
    {
        "text": (
            "Appendectomy is covered under "
            "surgical procedures."
        )
    },
    {
        "text": (
            "The maximum annual coverage limit "
            "is Rs. 5,00,000."
        )
    }
]


print("Calling local LLM...")

explanation = generate_claim_explanation(
    claim,
    decision,
    policy_evidence
)


print("\n==============================")
print("LOCAL LLM RESPONSE")
print("==============================")

print(explanation)