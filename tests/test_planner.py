from agents.planner import Planner

planner = Planner()

plan = planner.create_plan(
    "Analyze Microsoft's financial performance."
)

print(plan)