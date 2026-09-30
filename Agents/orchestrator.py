
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.state import ResearchState, ResearchTasks

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError("GROQ_API_KEY is missing. Add it to .env or set it in the environment.")

llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

structured_llm = llm.with_structured_output(ResearchTasks)

def orchestrator(state: ResearchState) -> ResearchState:
    question = state['question']
    
    prompt = f"""
            You are the orchestrator of a research assistant.
            Break the user's research question into 3-5
            specific research tasks.
            Each task should be independently researchable
            and useful for answering the original question.
            Research question:
            {question}
            """

    result = structured_llm.invoke(prompt)
    state["tasks"] = result.tasks

    return state