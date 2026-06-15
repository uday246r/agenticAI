from agno.agent import Agent
from agno.models.openai.responses import OpenAIResponses
from agno.models.groq import Groq
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

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
        tools=[DuckDuckGoTools(enable_search=True, enable_news=True)],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

openai_agent = build_agent()

openai_agent.print_response("Is it safe to travel UAE today ?")