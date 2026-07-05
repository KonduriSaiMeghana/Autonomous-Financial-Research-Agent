import ast

from agents.executor import Executor
from agents.planner import Planner

from tools.company_tool import CompanyTool
from tools.financial_tool import FinancialTool
from tools.news_tool import NewsTool
from tools.sec_tool import SECTool

from tools.tool_registry import ToolRegistry


registry = ToolRegistry()

registry.register(CompanyTool())
registry.register(FinancialTool())
registry.register(NewsTool())
registry.register(SECTool())


planner = Planner()

plan = planner.create_plan(
    "Analyze Microsoft as an investment."
)

plan = ast.literal_eval(plan)

executor = Executor(registry)

result = executor.execute_plan(
    plan,
    "MSFT"
)

print(result)