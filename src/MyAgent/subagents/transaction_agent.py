from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from src.MyAgent.schemas import State


model = init_chat_model("gpt-4", temperature=0)


transaction_agent = create_agent(
    model=model,
    tools=[fetch_transaction_id, get_transaction_info, update_jira_ticket],
    prompt=transaction_agent_prompt,
    name="Transaction_Agent",
    state_schema=State,
)


    