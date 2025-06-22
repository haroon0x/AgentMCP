from fastmcp import FastMCP

# This file is for non-core, reusable LLM prompt templates.

def register_prompts(mcp: FastMCP):
    @mcp.prompt
    def summarize_text(text: str) -> str:
        """Prompt template for summarizing text."""
        return f"Summarize the following text in one sentence:\n\n{text}" 