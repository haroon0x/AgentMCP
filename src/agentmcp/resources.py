from fastmcp import FastMCP

# This file is for non-core, read-only resources.

def register_resources(mcp: FastMCP):
    @mcp.resource("info://server")
    def server_info():
        """Return static server info resource."""
        return {
            "name": "AgentMCP",
            "version": "0.1.0",
            "description": "Non-core sample resource."
        } 