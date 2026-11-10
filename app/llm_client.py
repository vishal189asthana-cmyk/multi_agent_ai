
from langchain_ollama import ChatOllama

from app.prompts.llm_prompt import prompt


# Initialize local LLM
llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.2,
    base_url="http://localhost:11434"
)


# Create LangChain execution pipeline
chain = prompt | llm


def generate_response(question: str):

    response = chain.invoke({
        "question": question
    })

    return response.content
