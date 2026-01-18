import os
from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.groq import Groq
# from phi.llm.openai import OpenAIChat   # OpenAI
from phi.tools.hackernews import HackerNews

# Load environment variables
load_dotenv()

# =========================
# GROQ CONFIG (ACTIVE)
# =========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

llm = Groq(
    model="llama-3.1-8b-instant",  # stable + fast
    api_key=GROQ_API_KEY
)

# =========================
# OPENAI CONFIG
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
# HACKER NEWS ASSISTANT
# =========================
assistant = Assistant(
    llm=llm,
    tools=[HackerNews()],
    show_tool_calls=True,
    markdown=True,
)

# =========================
# QUERIES
# =========================
assistant.print_response(
    "Show me the top 5 Hacker News stories today with short summaries."
)

assistant.print_response(
    "What are the current trending topics on Hacker News?"
)

assistant.print_response(
    "Summarize the most interesting startup-related Hacker News stories."
)
