# tools/news_tool.py

from tavily import TavilyClient

from tools.base_tool import BaseTool
from config import TAVILY_API_KEY


class NewsTool(BaseTool):
    """
    Fetches the latest company news using Tavily Search.
    """

    def __init__(self):
        super().__init__(
            name="news_search",
            description="Searches the latest news about a company."
        )

        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    def execute(self, company: str):

        try:

            response = self.client.search(
                query=f"Latest news about {company}",
                search_depth="advanced",
                max_results=5
            )

            articles = []

            for result in response.get("results", []):

                articles.append({
                    "title": result.get("title"),
                    "url": result.get("url"),
                    "content": result.get("content")
                })

            return {
                "company": company,
                "articles": articles
            }

        except Exception as e:

            return {
                "error": str(e)
            }