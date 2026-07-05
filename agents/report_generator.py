# agents/report_generator.py

from langchain_groq import ChatGroq
from config import GROQ_API_KEY


class ReportGenerator:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model="llama-3.3-70b-versatile"
        )

    def generate_report(self, analysis, verification):

        prompt = f"""
You are a professional Financial Research Analyst.

Create a polished investment research report.

Use the following information.

------------------------------------

ANALYSIS

{analysis}

------------------------------------

VERIFICATION

{verification}

------------------------------------

Generate the report with these sections:

# Executive Summary

# Company Overview

# Financial Performance

# Recent Developments

# Risks

# Verification Summary

# Final Conclusion

IMPORTANT:

Do NOT invent facts.

Do NOT invent target prices.

Do NOT invent BUY/SELL recommendations.

Only use verified information.

Return the report in Markdown format.
"""

        response = self.llm.invoke(prompt)

        return response.content