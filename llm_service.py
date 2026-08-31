import ollama

def generate_claim_explanation(claim, policy_context, decision):

    prompt = f"""
You are an AI Insurance Approval Assistant.

Claim:
{claim}

Policy Information:
{policy_context}

Decision:
{decision}

Explain the decision clearly and briefly.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]