from langchain_groq import ChatGroq
from config import GROQ_API_KEY, LLM_MODEL



def get_llm():
    """
    Returns a configured Groq LLM instance.
    """
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL,
        temperature=0
    )
    