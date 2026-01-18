import os
import json
import streamlit as st
from dotenv import load_dotenv

from phi.llm.openai import OpenAIChat
from phi.assistant.duckdb import DuckDbAssistant

# Load environment variables
load_dotenv()

# Get API key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

# Create DuckDB Assistant
data_analyst = DuckDbAssistant(
    llm=OpenAIChat(
        model="gpt-4o",
        api_key=OPENAI_API_KEY
    ),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "imdb-top-1000.csv",
                }
            ]
        }
    ),
)

# Queries
data_analyst.print_response(
    "Highest rated movie in 2022? Show me the SQL.",
    markdown=True
)

data_analyst.print_response(
    "Different category of movies",
    markdown=True
)
