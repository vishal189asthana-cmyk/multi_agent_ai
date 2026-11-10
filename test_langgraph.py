from app.graph.workflow import workflow


initial_state = {
    "question": """
    Explain Delta Lake architecture.

    Cover:
    1. Transaction log
    2. ACID transactions
    3. Schema enforcement
    4. Time travel
    5. Performance optimization
    """,

    "research_notes": "",
    "analysis_report": "",
    "next_agent": ""
}


result = workflow.invoke(initial_state)


print("\n========== FINAL WORKFLOW RESULT ==========")

print("\nRESEARCH NOTES:\n")
print(result["research_notes"])

print("\nANALYSIS REPORT:\n")
print(result["analysis_report"])

print("\nFINAL SUPERVISOR DECISION:")
print(result["next_agent"])