# agents/verifier.py

from langchain_groq import ChatGroq
from config import GROQ_API_KEY


class Verifier:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model="llama-3.3-70b-versatile"
        )

    def verify(self, research_data, synthesized_report):

        prompt = f"""
You are a Senior Financial Auditor.

You are given:

1. Raw research data collected from tools.
2. A synthesized financial analysis.

RAW DATA

{research_data}

-------------------------------------------------

SYNTHESIZED REPORT

{synthesized_report}

-------------------------------------------------

Check for the following:

1. Hallucinated facts
2. Incorrect financial numbers
3. Missing important information
4. Contradictions
5. Unsupported recommendations
6. Missing citations

Return your response in this format:

Overall Confidence: XX%

Verified Facts
- ...

Potential Issues
- ...

Suggested Improvements
- ...
"""

        response = self.llm.invoke(prompt)

        return response.content