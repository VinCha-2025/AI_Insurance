from claim_processor import process_claim


claim = {
    "age": 45,
    "diagnosis": "Appendicitis",
    "procedure": "Appendectomy",
    "claim_amount": 80000
}


result = process_claim(claim)


print("\n================================")
print("AI INSURANCE CLAIM RESULT")
print("================================")

print(
    "\nDecision:",
    result["decision"]["decision"]
)

print(
    "\nRule Engine Reason:",
    result["decision"]["reason"]
)

print(
    "\nAI Explanation:",
    result["explanation"]
)


print("\nPolicy Evidence:")

for evidence in result["policy_evidence"]:

    print("\n------------------------")
    print(evidence["text"])