import os
import requests
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query: str) -> list[dict]:
    """Search the web using Tavily. Returns a list of search results containing title, URL and content."""

    if not query.strip():
        raise ValueError("Search query cannot be empty.")

    results = tavily_client.search(
        query=query,
        max_results=2
    )

    cleaned_results = []

    for item in results.get("results", []):
        cleaned_results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", "")
        })

    return cleaned_results




def read_url(url: str) -> str:
    """Fetch the content of a webpage."""

    if not url.strip():
        raise ValueError("URL cannot be empty.")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text

    except requests.RequestException as e:
        raise RuntimeError(f"Failed to read URL: {e}")