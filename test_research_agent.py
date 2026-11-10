
from app.agents.research_agent import research_agent


question = """
Explain Delta Lake architecture.

Cover:
1. Delta Lake
2. Transaction log
3. ACID transactions
4. Schema enforcement
5. Time travel
6. Practical data engineering example
"""


result = research_agent(question)


print("\n========== RESEARCH AGENT ==========\n")

print("Agent:", result["agent"])

print("\nResearch Notes:\n")

print(result["research_notes"])

print("\nStatus:", result["status"])
