
from langchain_core.prompts import ChatPromptTemplate

from app.llm_client import llm


# Analysis Agent prompt
analysis_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are an expert Technical Analysis Agent.

        Your responsibility is to analyze research
        provided by another AI agent.

        Analyze the research using these criteria:

        1. Technical correctness
        2. Completeness
        3. Missing information
        4. Technical limitations
        5. Implementation risks
        6. Practical business implications

        Important rules:

        - Do not simply repeat the research.
        - Identify missing concepts.
        - Highlight unsupported claims.
        - Do not invent facts.
        - Clearly identify uncertainty.
        - Provide actionable recommendations.

        Return a structured analysis.
        """
    ),

    (
        "human",
        """
        Original Question:

        {question}

        Research Agent Output:

        {research_notes}

        Analyze the research and prepare a detailed report.
        """
    )

])


# Create analysis chain
analysis_chain = analysis_prompt | llm


# Analysis Agent function
def analysis_agent(question: str, research_notes: str):

    response = analysis_chain.invoke({

        "question": question,

        "research_notes": research_notes

    })

    return {

        "agent": "analysis_agent",

        "analysis_report": response.content,

        "status": "completed"

    }
