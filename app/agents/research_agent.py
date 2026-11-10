
from langchain_core.prompts import ChatPromptTemplate

from app.llm_client import llm


# Research Agent system prompt
research_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are an expert Research Agent specializing
        in Data Engineering and AI.

        Your responsibilities:

        1. Understand the research question.
        2. Identify important concepts.
        3. Explain technical components.
        4. Identify advantages and limitations.
        5. Provide practical examples.
        6. Highlight uncertain or unverified information.

        Rules:

        - Do not invent facts.
        - Do not fabricate sources.
        - Clearly distinguish established facts
          from assumptions.
        - Keep the research structured.
        """
    ),

    (
        "human",
        """
        Research Question:

        {question}

        Prepare structured research notes.
        """
    )

])


# Create research chain
research_chain = research_prompt | llm


# Research Agent function
def research_agent(question: str):

    response = research_chain.invoke({

        "question": question

    })

    return {

        "agent": "research_agent",

        "research_notes": response.content,

        "status": "completed"

    }
