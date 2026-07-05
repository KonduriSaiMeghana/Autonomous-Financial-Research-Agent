# tools/financial_tool.py

import yfinance as yf
from tools.base_tool import BaseTool


class FinancialTool(BaseTool):
    """
    Fetches key financial metrics using Yahoo Finance.
    """

    def __init__(self):
        super().__init__(
            name="financial_data",
            description="Retrieves financial statements and key metrics."
        )

    def execute(self, ticker: str):

        try:
            stock = yf.Ticker(ticker)

            info = stock.info
            financials = stock.financials
            balance_sheet = stock.balance_sheet

            revenue = None
            net_income = None
            total_assets = None
            total_debt = None
            cash = None

            # Income Statement
            if not financials.empty:

                if "Total Revenue" in financials.index:
                    revenue = financials.loc["Total Revenue"].iloc[0]

                if "Net Income" in financials.index:
                    net_income = financials.loc["Net Income"].iloc[0]

            # Balance Sheet
            if not balance_sheet.empty:

                if "Total Assets" in balance_sheet.index:
                    total_assets = balance_sheet.loc["Total Assets"].iloc[0]

                if "Total Debt" in balance_sheet.index:
                    total_debt = balance_sheet.loc["Total Debt"].iloc[0]

                if "Cash And Cash Equivalents" in balance_sheet.index:
                    cash = balance_sheet.loc["Cash And Cash Equivalents"].iloc[0]

            return {

                "ticker": ticker.upper(),

                "current_price": info.get("currentPrice"),

                "previous_close": info.get("previousClose"),

                "market_cap": info.get("marketCap"),

                "revenue": float(revenue) if revenue is not None else None,
                "net_income": float(net_income) if net_income is not None else None,
                "total_assets": float(total_assets) if total_assets is not None else None,
                "total_debt": float(total_debt) if total_debt is not None else None,
                "cash": float(cash) if cash is not None else None,
            }

        except Exception as e:

            return {
                "error": str(e)
            }