import ast

from agents.planner import Planner
from agents.executor import Executor
from agents.synthesizer import Synthesizer

from tools.company_tool import CompanyTool
from tools.financial_tool import FinancialTool
from tools.news_tool import NewsTool
from tools.sec_tool import SECTool
from tools.tool_registry import ToolRegistry

# Register tools
registry = ToolRegistry()
registry.register(CompanyTool())
registry.register(FinancialTool())
registry.register(NewsTool())
registry.register(SECTool())

# Planner
planner = Planner()
plan = planner.create_plan("Analyze Microsoft (MSFT) as an investment.")
plan = ast.literal_eval(plan)

# Executor
executor = Executor(registry)
results = executor.execute_plan(plan, "MSFT")

# Synthesizer
synthesizer = Synthesizer()
analysis = synthesizer.synthesize(results)

print(analysis)