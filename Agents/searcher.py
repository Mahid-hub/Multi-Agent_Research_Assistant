from dotenv import load_dotenv
from tavily import TavilyClient
from src.state import ResearchState
import os

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(state: ResearchState) -> ResearchState:
    results = tavily_client.search(
        query=state['tasks'][0],
        max_results=5
    )

    state['search_result'] = results
    return state

# if __name__ == "__main__":
#     task = "Research current applications of generative AI in healthcare"

#     results = search_web(task)

#     print("\nSearch Results:")

#     for result in results["results"]:
#         print("\nTitle:", result["title"])
#         print("URL:", result["url"])
#         print("Content:", result["content"])