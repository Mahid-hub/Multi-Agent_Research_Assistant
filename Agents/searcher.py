from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(task: str):
    results = tavily_client.search(
        query=task,
        max_results=5
    )

    return results

if __name__ == "__main__":
    task = input("Search task: ")

    results = search_web(task)

    print("\nSearch Results:")

    for result in results["results"]:
        print("\nTitle:", result["title"])
        print("URL:", result["url"])
        print("Content:", result["content"])