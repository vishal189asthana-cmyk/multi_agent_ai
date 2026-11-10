from typing import TypedDict


class AgentState(TypedDict):
    question: str

    research_notes: str
    analysis_report: str

    next_agent: str