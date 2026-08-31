from decision_engine import evaluate_claim


claim = {
    "age": 45,
    "diagnosis": "Appendicitis",
    "procedure": "Appendectomy",
    "claim_amount": 80000
}


result = evaluate_claim(claim)


print("Decision:", result["decision"])
print("Reason:", result["reason"])