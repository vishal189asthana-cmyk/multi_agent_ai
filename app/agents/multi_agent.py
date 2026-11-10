
from app.agents.research_agent import research_agent

from app.agents.analysis_agent import analysis_agent


def run_multi_agent(question: str):

    # Step 1: Execute Research Agent
    research_result = research_agent(question)

    research_notes = research_result["research_notes"]


    # Step 2: Execute Analysis Agent
    analysis_result = analysis_agent(
        question=question,
        research_notes=research_notes
    )


    # Step 3: Collect results
    return {

        "question": question,

        "research": research_result,

        "analysis": analysis_result,

        "status": "completed"

    }
