import os
from dotenv import load_dotenv

from phi.assistant import Assistant
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
    model="llama-3.1-8b-instant",  # fast, free
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

assistant = Assistant(
    llm=llm,
    description="You are a famous short story writer asked to write for a magazine.",
    instructions=[
        "You are a pilot on a plane flying from Hawaii to Japan."
    ],
    markdown=True,
    debug_mode=True,
)

assistant.print_response(
    "Tell me a 2 sentence horror story."
)
