
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import asyncio

from app.llm_client import chain
from app.agents.research_agent import research_agent


# 1. Define request schema
class QuestionRequest(BaseModel):
    question: str = Field(min_length=5, max_length=1000)
    user_id: str


# 2. Create FastAPI application
app = FastAPI(
    title="Multi Agent AI System",
    description="FastAPI application with LangChain and LangGraph",
    version="1.0.0"
)


# 3. Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Multi Agent AI System"}


# 4. Health endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "multi-agent-ai"
    }


# 5. Basic LLM endpoint
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        response = await chain.ainvoke({
            "question": request.question
        })

        return {
            "user_id": request.user_id,
            "question": request.question,
            "answer": response.content,
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=str(e)
        )


# 6. Research Agent endpoint
@app.post("/research")
async def run_research(request: QuestionRequest):
    try:
        result = await asyncio.to_thread(
            research_agent,
            request.question
        )

        return {
            "user_id": request.user_id,
            "question": request.question,
            "research": result,
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
