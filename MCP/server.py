from mcp.server.mcpserver import MCPServer
from MCP.tools import web_search, read_url

mcp = MCPServer(
    name="Research Tools Server",
    version="1.0.0",
)

@mcp.tool()
def search_web(query: str) -> list[dict]:
    """Search the web using Tavily."""
    return web_search(query=query)

@mcp.tool()
def fetch_url(url: str) -> str:
    """Fetch webpage content from a URL."""

    return read_url(url)

if __name__ == "__main__":
    mcp.run("stdio")