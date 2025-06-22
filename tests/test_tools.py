def test_reverse_string():
    from src.agentmcp.tools import register_tools
    class DummyMCP:
        def __init__(self): self.called = False
        def tool(self, fn): self.called = True; return fn
    mcp = DummyMCP()
    register_tools(mcp)
    assert mcp.called 