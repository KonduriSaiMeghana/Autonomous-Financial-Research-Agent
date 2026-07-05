# agents/planner.py

from langchain_groq import ChatGroq

from config import GROQ_API_KEY


class Planner:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model="llama-3.3-70b-versatile"
        )

    def create_plan(self, user_query: str):

        prompt = f"""
You are a Financial Research Planner.

The available tools are:

1. company_profile
2. financial_data
3. news_search
4. sec_filings

User Query:
{user_query}

Return ONLY a Python list containing the tools that should be executed.

Example:

["company_profile","financial_data","news_search"]
"""

        response = self.llm.invoke(prompt)

        return response.content