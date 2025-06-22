from fastmcp import FastMCP

# This file is for non-core, utility tools that can be mounted or imported into the main server.

def register_tools(mcp: FastMCP):
    @mcp.tool
    def reverse_string(text: str) -> str:
        """Reverse the input string."""
        return text[::-1] 