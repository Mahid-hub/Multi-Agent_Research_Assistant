# import os
# from dotenv import load_dotenv
# from tavily import TavilyClient
from ddgs import DDGS
from src.state import ResearchState

# load_dotenv()
# tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(state: ResearchState) -> ResearchState:
    search_results = []
    
    for task in state['tasks']:
        search_query = f"{state['question']} {task}"
        
        results = DDGS().text(
            search_query,
            max_results=5
        )
        
        search_results.append({
            "task": task,
            "results": results
        })
    # results = tavily_client.search(
    #     query=task,
    #     max_results=5
    # )

    state['search_result'] = search_results
    return state
