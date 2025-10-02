from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from src.MyAgent.schemas import State


model = init_chat_model("gpt-4", temperature=0)

# this agent will handle company info related quries using rag
company_info_agent = create_agent(
    model=model,
    tools=[fetch_company, update_jira_ticket],
    prompt=company_info_agent_prompt,
    state_schema=State,
    name="company_info_agent",
)


    