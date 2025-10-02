from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from src.MyAgent.schemas import State



model = init_chat_model("gpt-4", temperature=0)

# this agent will handle delivery related quries
delivery_agent = create_agent(
    model=model,
    tools=[fetch_order_id, get_order_info, update_jira_ticket],
    prompt=delivery_agent_PROMPT,
     state_schema=State,
    name="delivery_Agent",
)


    