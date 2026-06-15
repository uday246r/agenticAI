from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from pprint import pprint

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3-32b"),
        markdown=True,
        add_history_to_context=True,
        enable_user_memories=True
    )

agent = build_agent()

user_id="uday@gmail.com"

agent.print_response("My name is Uday and i am Full Stack Developer at RM Applications Malaysia", user_id=user_id)
agent.print_response("Who am i?", user_id=user_id)

memories = agent.get_user_memories(
    user_id=user_id
)

print("MEMORIES: ")
pprint(memories)