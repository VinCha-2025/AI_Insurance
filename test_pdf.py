from rag.pdf_loader import load_pdf


pdf_path = "data/policies/Health_policy.pdf"

text = load_pdf(pdf_path)

print("====================================")
print("       HEALTH POLICY CONTENT")
print("====================================")

print(text)

print("====================================")
print("       PDF READING COMPLETE")
print("====================================")