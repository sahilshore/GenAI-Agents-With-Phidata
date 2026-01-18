import os
from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.llm.groq import Groq
# from phi.llm.openai import OpenAIChat  # OpenAI 
load_dotenv()

# =========================
# GROQ CONFIG
# =========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

llm = Groq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY
)

# =========================
# KNOWLEDGE BASE (FIXED DB URL)
# =========================
knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        "https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"
    ],
    vector_db=PgVector2(
        collection="recipes",
        db_url="postgresql+psycopg2://ai:ai@localhost:5532/ai",  # ✅ FIX
    ),
)

knowledge_base.load(recreate=False)

# =========================
# RAG ASSISTANT
# =========================
assistant = Assistant(
    llm=llm,
    knowledge_base=knowledge_base,
    add_references_to_prompt=True,
    markdown=True,
)

assistant.print_response(
    "What are the ingredients to make Massaman Gai?"
)
