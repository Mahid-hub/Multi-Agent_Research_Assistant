import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.state import ReaderResult, ResearchState

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

structured_llm = llm.with_structured_output(ReaderResult)

def reader(state: ResearchState) -> ResearchState:
    reader_results = []
    
    for item in state["search_result"]:
        result = read_content(item["body"])

        reader_results.append({
            "title": item["title"],
            "url": item["href"],
            "summary": result.summary,
        })
    
    state['reader_results'] = reader_results
    return state

def read_content(content: str) -> ReaderResult:
    prompt = f"""
You are the Reader Agent in a multi-agent research assistant.
Analyze the provided research content.
Extract the important information that would help
answer the original research task.
Provide:
1. A concise summary.
2. The most important key points.
Do not invent information.
Research content:
{content}
"""

    result = structured_llm.invoke(prompt)
    return result