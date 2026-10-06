import os
import sys
import asyncio
from pathlib import Path
from mcp import Client, StdioServerParameters

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SERVER_PATH = PROJECT_ROOT / "MCP" / "server.py"

def get_server_parameters() -> StdioServerParameters:
    """Create configuration for launching the MCP server."""
    
    env = os.environ.copy()
    return StdioServerParameters(
        command=sys.executable,
        args=["-m", "MCP.server"],
        env=env,
        cwd=str(PROJECT_ROOT),
    )

async def main():
    server_params = get_server_parameters()
    async with Client(server_params) as client:
        print("MCP session initialized.")
        print("\nAvailable MCP tools:")

        tools_result = await client.list_tools()
        for tool in tools_result.tools:
            print(f"- {tool.name}")
            
if __name__ == "__main__":
    asyncio.run(main())