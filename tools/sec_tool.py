from tavily import TavilyClient

from config import TAVILY_API_KEY
from tools.base_tool import BaseTool


class SECTool(BaseTool):

    def __init__(self):
        super().__init__(
            name="sec_filings",
            description="Retrieves latest SEC filings."
        )

        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    def execute(self, company: str):

        try:

            response = self.client.search(
                query=f"{company} latest 10-K SEC filing site:sec.gov",
                search_depth="advanced",
                max_results=3
            )

            filings = []

            for result in response.get("results", []):

                filings.append({
                    "title": result.get("title"),
                    "url": result.get("url"),
                    "content": result.get("content")
                })

            return {
                "company": company,
                "filings": filings
            }

        except Exception as e:

            return {
                "error": str(e)
            }