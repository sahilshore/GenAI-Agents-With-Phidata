# IF YOU HAVE GROQ API KEY THEN USE THIS CODE !!!!!! 

import os
from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.groq import Groq
from phi.tools.yfinance import YFinanceTools

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

assistant = Assistant(
    llm=Groq(
        model="llama-3.1-8b-instant",  # best Groq model
        api_key=GROQ_API_KEY
    ),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True
        )
    ],
    show_tool_calls=True,
    markdown=True,
)

assistant.print_response("What is the stock price of NVDA")
assistant.print_response(
    "Write a comparison between NVDA and AMD, use all tools available."
)

# IF YOU HAVE OPENAI API KEY THEN USE BELOW  CODE !!!!!! 

# import os
# from dotenv import load_dotenv

# from phi.assistant import Assistant
# from phi.llm.openai import OpenAIChat
# from phi.tools.yfinance import YFinanceTools

# # Load env
# load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# if not OPENAI_API_KEY:
#     raise ValueError("OPENAI_API_KEY not found in .env")

# assistant = Assistant(
#     llm=OpenAIChat(
#         model="gpt-4o-mini",   # cheaper
#         api_key=OPENAI_API_KEY
#     ),
#     tools=[
#         YFinanceTools(
#             stock_price=True,
#             analyst_recommendations=True,
#             company_info=True,
#             company_news=True
#         )
#     ],
#     show_tool_calls=True,
#     markdown=True,
# )

# assistant.print_response("What is the stock price of NVDA")
# assistant.print_response(
#     "Write a comparison between NVDA and AMD, use all tools available."
# )
