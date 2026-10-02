import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.state import ReaderResult, ResearchState
from langfuse import observe

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

@observe(name="Reader", as_type="agent")
def reader(state: ResearchState) -> ResearchState:
    if not state["search_result"]:
        raise ValueError("No search results available.")
    
    reader_results = []
    try:
        for searchResult in state['search_result']:
            task = searchResult['task']
        
            for item in searchResult["results"]:
                if not item.get("content"):
                    print(f"No content available for: {item['title']}")
                    continue

                result = read_content(item["content"])
                reader_results.append({
                    "task": task,
                    "title": item["title"],
                    "url": item["url"],
                    "summary": result.summary,
                })
        
        state['reader_results'] = reader_results
        return state
    
    except Exception as e:
        print(f"Reader error: {e}")
        raise

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