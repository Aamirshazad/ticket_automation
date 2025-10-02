from typing import Literal

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage

from langgraph.types import Command
from langgraph.graph import START,END, StateGraph


from MyAgent.tools.default.jsearch_tools import search_files
from src.MyAgent.prompts import router_prompt
from src.MyAgent.schemas import RouterSchema, State
from src.MyAgent.subagents.company_info_agent import company_info_agent
from src.MyAgent.subagents.delivery_agent import delivery_agent
from src.MyAgent.subagents.order_agent import order_agent
from src.MyAgent.subagents.transaction_agent import transaction_agent



llm = init_chat_model("openai:gpt-4.1")
llm_router = llm.with_structured_output(RouterSchema)


def ticket_router_agent(state: State) -> Command[Literal["company_info_agent", "delivery_agent", "order_agent", "transaction_agent"]]:
    """
    This agent will route the query to the appropriate sub-agent based on the user's request.
    It uses a schema to determine which sub-agent to call and what input to provide.
    """

    response = llm_router.invoke(
        [
            SystemMessage(content=router_prompt),
        ]+
        state["messages"]
    )
    
    result = response.router

    if result == "company_info_agent":
        goto = "company_info_agent"
    elif result == "delivery_agent":
        goto = "delivery_agent"
    elif result == "order_agent":
        goto = "order_agent"
    elif result == "transaction_agent":
        goto = "transaction_agent"
    else:
        raise ValueError(f"Unknown agent: {result}")
    
    return Command(goto=goto, update={"router": result}) 


workflow = StateGraph(State)
workflow.add_node("ticket_router_agent",ticket_router_agent)
workflow.add_node("company_info_agent",company_info_agent)
workflow.add_node("delivery_agent",delivery_agent)
workflow.add_node("order_agent",order_agent)
workflow.add_node("transaction_agent",transaction_agent)

workflow.add_edge(START, "ticket_router_agent")

agent = workflow.compile()
