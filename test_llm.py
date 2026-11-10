
from app.llm_client import generate_response

question = "Explain multi-agent architecture in simple terms."

answer = generate_response(question)

print("\n========== AI RESPONSE ==========\n")
print(answer)
