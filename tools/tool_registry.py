# tools/tool_registry.py

from typing import Dict
from tools.base_tool import BaseTool


class ToolRegistry:
    """
    Stores and manages all tools used by the agent.
    """

    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):
        """
        Register a new tool.
        """

        if tool.name in self.tools:
            raise ValueError(f"Tool '{tool.name}' is already registered.")

        self.tools[tool.name] = tool

    def get_tool(self, tool_name: str):
        """
        Return a tool by its name.
        """

        return self.tools.get(tool_name)

    def list_tools(self):
        """
        Return all registered tool names.
        """

        return list(self.tools.keys())

    def remove_tool(self, tool_name: str):
        """
        Remove a tool.
        """

        if tool_name in self.tools:
            del self.tools[tool_name]

    def has_tool(self, tool_name: str):
        """
        Check if tool exists.
        """

        return tool_name in self.tools