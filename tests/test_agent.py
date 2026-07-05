from agent import FinancialResearchAgent

agent = FinancialResearchAgent()

report = agent.run(

    ticker="MSFT",

    query="Analyze Microsoft (MSFT) as an investment."

)

print(report)