import os
import asyncio
from MCP.client import Client, get_server_parameters
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

async def fetch_url(url):
    server_params = get_server_parameters()

    async with Client(server_params) as client:
        result = await client.call_tool("fetch_url", {"url": url})
        return result
    
    
@observe(name="Reader", as_type="agent")
def reader(state: ResearchState) -> ResearchState:
    if not state["search_result"]:
        raise ValueError("No search results available.")
    
    reader_results = []
    try:
        for searchResult in state['search_result']:
            task = searchResult['task']
        
            for item in searchResult["results"]:
                url = item.get("url")
                if not url:
                    print("No URL available.")
                    continue

                result = asyncio.run(fetch_url(url))
                content = result.content[0].text[:5000]
                summary = read_content(content)
                
                reader_results.append({
                    "task": task,
                    "title": item["title"],
                    "url": url,
                    "summary": summary.summary,
                })
        
        state['reader_results'] = reader_results
        return state
    
    except Exception as e:
        print(f"Reader error: {e}")
        raise

def read_content(content: str) -> ReaderResult:
    prompt = f"""
            You are the Reader Agent in a multi-agent research assistant.
            Analyze the provided research content and extract the important
            information that would help answer the research task.
            Return a concise summary containing the important facts.
            Do not invent information.
            Only use information from the provided content.
            Research content:
            {content}
            """

    result = structured_llm.invoke(prompt)
    return result