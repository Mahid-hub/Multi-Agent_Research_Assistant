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
