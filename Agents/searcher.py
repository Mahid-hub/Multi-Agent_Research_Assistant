import os
from dotenv import load_dotenv
from tavily import TavilyClient
from src.state import ResearchState
from langfuse import observe

load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@observe(name="Searcher", as_type="tool")
def search_web(state: ResearchState) -> ResearchState:
    if not state["tasks"]:
        raise ValueError("No research tasks available.")
    
    search_results = []
    
    for task in state['tasks']:        
        results = tavily_client.search(
            query=task,
            max_results=5
        )
        
        if not results["results"]:
            print(f"No results found for: {task}")
    
        search_results.append({
            "task": task,
            "results": results["results"] 
        })

    state['search_result'] = search_results
    return state
