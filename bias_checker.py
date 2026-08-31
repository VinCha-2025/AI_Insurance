def compare_claims(claim1, claim2):

    important_fields = [
        "diagnosis",
        "procedure",
        "claim_amount"
    ]

    same_claim_information = all(
        claim1[field] == claim2[field]
        for field in important_fields
    )

    if not same_claim_information:

        return {
            "bias_check": "NOT APPLICABLE",
            "message": (
                "Claims contain different "
                "claim-relevant information."
            )
        }

    return {
        "bias_check": "READY",
        "message": (
            "Claims have identical claim-relevant "
            "information and can be compared."
        )
    }