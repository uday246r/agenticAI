from agno.agent import Agent
from agno.models.openai.responses import OpenAIResponses
from agno.models.groq import Groq
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
    #      model=Gemini(
    #     id="gemini-2.0-flash",
    #     # vertexai=True,
    #     project_id="gen-lang-client-0736553335",
    #     location="us-central1",
    # ),
        # model=OpenAIResponses(id="gpt-5-mini"),
        # model=Groq(id="llama-3.3-70b-versatile"),
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YFinanceTools(),DuckDuckGoTools()],
        markdown=True,
         add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use given tools whenever possible. Format your response using markdown and use tables to display data where possible."],
        debug_node=True
    )

agent = build_agent()

agent.print_response("Share the MSFT stock price and analyst recommendations")