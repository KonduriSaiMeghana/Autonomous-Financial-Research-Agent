# config.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -------------------------
# API Keys
# -------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# -------------------------
# Model Configuration
# -------------------------

LLM_MODEL = "llama-3.3-70b-versatile"

# -------------------------
# Memory Configuration
# -------------------------

VECTOR_DB_PATH = "memory/faiss_index"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# -------------------------
# Agent Configuration
# -------------------------

MAX_ITERATIONS = 10

MAX_RETRIES = 3