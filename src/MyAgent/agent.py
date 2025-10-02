from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from src.MyAgent.tools.default.email_tools import search_files
from src.MyAgent.prompts import system_prompt

model = init_chat_model("openai:gpt-4.1")



graph = create_agent(
    model=model,
    tools=[search_files],
    prompt=system_prompt

)
