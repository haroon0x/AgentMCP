from fastmcp import FastMCP
from src.agentmcp.tools import register_tools
from src.agentmcp.resources import register_resources
from src.agentmcp.prompts import register_prompts

mcp = FastMCP("🧠 AgentMCP Server")

register_tools(mcp)
register_resources(mcp)
register_prompts(mcp)


@mcp.tool
def hello(name: str = "World") -> str:
    """A simple hello tool."""
    return f"Hello, {name}!"



def run_server():
    """Run the FastMCP server."""
    mcp.run() 

