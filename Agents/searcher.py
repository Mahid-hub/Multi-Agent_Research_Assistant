# import os
# from dotenv import load_dotenv
# from tavily import TavilyClient
from ddgs import DDGS
from src.state import ResearchState

# load_dotenv()
# tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(state: ResearchState) -> ResearchState:
    results = DDGS().text(
        state['tasks'][0],
        max_results=5
    )
    # results = tavily_client.search(
    #     query=state['tasks'][0],
    #     max_results=5
    # )

    state['search_result'] = results
    return state
