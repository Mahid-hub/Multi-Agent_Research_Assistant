import json
import asyncio

from langgraph.func import task
from src.state import ResearchState
from MCP.client import Client, get_server_parameters
from langfuse import observe

async def call_search_tool(query):
    server_params = get_server_parameters()

    async with Client(server_params) as client:
        result = await client.call_tool(
            "search_web",
            {
                "query": query,
                "max_results": 2
            }
)

        return result
    
@observe(name="Searcher", as_type="tool")
def search_web(state: ResearchState) -> ResearchState:
    if not state["tasks"]:
        raise ValueError("No research tasks available.")
    
    try:
        search_results = []
        
        for task in state['tasks']:        
            result = asyncio.run(call_search_tool(task))
            results = []

            for content_item in result.content:
                item = json.loads(content_item.text)
                results.append(item)

            if not results:
                print(f"No results found for: {task}")

            search_results.append({
                "task": task,
                "results": results
            })

        state["search_result"] = search_results
        return state
    
    except Exception as e:
        print(f"Searcher error: {e}")
        raise