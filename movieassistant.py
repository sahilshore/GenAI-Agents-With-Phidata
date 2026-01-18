import os
import json
from dotenv import load_dotenv

from phi.assistant.duckdb import DuckDbAssistant
from phi.llm.groq import Groq
# from phi.llm.openai import OpenAIChat  # OpenAI 
# Load environment variables
load_dotenv()

# =========================
# GROQ CONFIG (ACTIVE)
# =========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

llm = Groq(
    model="llama-3.1-8b-instant",  # fast + free
    api_key=GROQ_API_KEY
)

# =========================
# OPENAI CONFIG (COMMENTED)
# =========================
"""
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")

llm = OpenAIChat(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)
"""

# =========================
# MOVIE ASSISTANT (DuckDB)
# =========================
movie_assistant = DuckDbAssistant(
    llm=llm,
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Top 1000 movies from IMDB with ratings, genres, directors, and release year.",
                    "path": "imdb-top-1000.csv",
                }
            ]
        }
    ),
    markdown=True,
    show_sql=True,   # shows generated SQL (very good for learning)
)

# =========================
# EXAMPLE QUERIES
# =========================
movie_assistant.print_response(
    "What are the top 5 highest rated movies overall?"
)

movie_assistant.print_response(
    "Which movies released after 2015 have IMDb rating above 8?"
)

movie_assistant.print_response(
    "Show the top 5 directors by average IMDb rating."
)

movie_assistant.print_response(
    "List different movie genres available in the dataset."
)
