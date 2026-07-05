# app.py

from financial_agent import FinancialResearchAgent


def main():

    print("=" * 60)
    print("      AI Financial Research Agent")
    print("=" * 60)

    ticker = input("\nEnter Company Ticker (e.g., MSFT): ").strip().upper()

    query = input("\nEnter your research query:\n> ").strip()

    if not query:
        query = f"Analyze {ticker} as an investment."

    agent = FinancialResearchAgent()

    report = agent.run(
        ticker=ticker,
        query=query
    )

    print("\n" + "=" * 60)
    print("FINAL REPORT")
    print("=" * 60)
    print(report)


if __name__ == "__main__":
    main()