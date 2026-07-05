# tools/company_tool.py

import yfinance as yf
from tools.base_tool import BaseTool


class CompanyTool(BaseTool):
    """
    Fetches basic company profile information using Yahoo Finance.
    """

    def __init__(self):
        super().__init__(
            name="company_profile",
            description="Fetches company profile information."
        )

    def execute(self, ticker: str):

        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            return {
                "ticker": ticker.upper(),
                "company_name": info.get("longName"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "country": info.get("country"),
                "website": info.get("website"),
                "employees": info.get("fullTimeEmployees"),
                "market_cap": info.get("marketCap"),
                "summary": info.get("longBusinessSummary")
            }

        except Exception as e:
            return {
                "error": str(e)
            }