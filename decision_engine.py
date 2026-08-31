def evaluate_claim(claim):
    """
    Basic rule-based claim evaluation.
    """

    diagnosis = claim["diagnosis"].lower()
    procedure = claim["procedure"].lower()
    amount = claim["claim_amount"]

    reasons = []

    # Coverage limit
    if amount > 500000:
        return {
            "decision": "MANUAL REVIEW",
            "reason": "Claim amount exceeds the annual coverage limit."
        }

    # Check surgical procedure
    covered_procedures = [
        "appendectomy",
        "hernia repair",
        "gallbladder surgery",
        "cataract surgery",
        "knee replacement",
        "emergency fracture surgery"
    ]

    procedure_covered = False

    for covered in covered_procedures:
        if covered in procedure:
            procedure_covered = True
            break

    if procedure_covered:
        reasons.append(
            "The requested surgical procedure is listed as covered."
        )
    else:
        return {
            "decision": "MANUAL REVIEW",
            "reason": "The requested procedure is not clearly listed as covered."
        }

    # Check diagnosis
    if diagnosis:
        reasons.append(
            "A medical diagnosis was provided."
        )
    else:
        return {
            "decision": "MANUAL REVIEW",
            "reason": "Diagnosis is missing."
        }

    return {
        "decision": "APPROVED",
        "reason": " ".join(reasons)
    }