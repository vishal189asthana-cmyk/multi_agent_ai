from app.agents.research_agent import research_agent
from app.agents.analysis_agent import analysis_agent


# Research node: runs the Research Agent and saves its notes
def research_node(state):

    print("\n--- Research Agent Executing ---")

    result = research_agent(state["question"])

    return {
        "research_notes": result["research_notes"]
    }


# Analysis node: runs the Analysis Agent on the research notes
def analysis_node(state):

    print("\n--- Analysis Agent Executing ---")

    result = analysis_agent(
        question=state["question"],
        research_notes=state["research_notes"]
    )

    return {
        "analysis_report": result["analysis_report"]
    }
