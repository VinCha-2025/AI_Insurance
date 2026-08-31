from fastapi import FastAPI
from pydantic import BaseModel

from claim_processor import process_claim


app = FastAPI(
    title="AI Health Insurance Claim Approval System",
    description="AI-powered insurance claim processing API",
    version="1.0"
)


class Claim(BaseModel):

    age: int

    diagnosis: str

    procedure: str

    claim_amount: float


@app.get("/")
def home():

    return {
        "message": "AI Health Insurance Claim Approval API"
    }


@app.post("/claims")
def process_insurance_claim(claim: Claim):

    claim_data = claim.model_dump()

    result = process_claim(claim_data)

    return result