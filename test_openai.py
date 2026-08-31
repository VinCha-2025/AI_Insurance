import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY was not found.")
    exit()

print("API key found.")

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Say hello in one sentence."
    )

    print("OpenAI connection successful!")
    print(response.output_text)

except Exception as e:
    print("OpenAI connection failed:")
    print(e)