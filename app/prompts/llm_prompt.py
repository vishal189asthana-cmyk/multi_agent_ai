
from langchain_core.prompts import ChatPromptTemplate

# Define the system and user prompts
prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are a helpful AI assistant.

        Your responsibilities:
        1. Understand the user's question.
        2. Provide accurate and simple explanations.
        3. Avoid inventing facts.
        4. If you are unsure, clearly mention uncertainty.
        5. Structure answers using examples where useful.
        """
    ),

    (
        "human",
        "{question}"
    )

])
