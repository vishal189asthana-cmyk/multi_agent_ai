
from app.agents.multi_agent import run_multi_agent


question = """
Explain Delta Lake architecture for a data engineering project.

Cover:
- Transaction log
- ACID transactions
- Schema enforcement
- Time travel
- Performance optimization
"""


result = run_multi_agent(question)


print("\n========== USER QUESTION ==========")

print(result["question"])


print("\n========== RESEARCH AGENT ==========")

print(result["research"]["research_notes"])


print("\n========== ANALYSIS AGENT ==========")

print(result["analysis"]["analysis_report"])


print("\n========== WORKFLOW STATUS ==========")

print(result["status"])
