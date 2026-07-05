# agents/executor.py

from tools.tool_registry import ToolRegistry


class Executor:

    def __init__(self, registry: ToolRegistry):

        self.registry = registry

    def execute_plan(self, plan, company):

        results = {}

        for tool_name in plan:

            tool = self.registry.get_tool(tool_name)

            if tool is None:

                results[tool_name] = {
                    "error": f"{tool_name} not found."
                }

                continue

            results[tool_name] = tool.execute(company)

        return results