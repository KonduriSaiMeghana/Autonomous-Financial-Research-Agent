# agents/synthesizer.py

from langchain_groq import ChatGroq
from config import GROQ_API_KEY


class Synthesizer:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model="llama-3.3-70b-versatile"
        )

    def synthesize(self, research_data):

        prompt = f"""
You are a Senior Financial Research Analyst.

Below is research collected from multiple sources.

Research Data:

{research_data}

Your task:

1. Combine all information.
2. Remove duplicate information.
3. Highlight important financial insights.
4. Mention recent developments.
5. Mention potential risks.
6. Write a professional investment analysis.

Return only the analysis.
"""

        response = self.llm.invoke(prompt)

        return response.content