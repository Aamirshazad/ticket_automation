from pydantic import BaseModel, Field
from typing_extensions import TypedDict, Literal
from langgraph.graph import MessagesState



class RouterSchema(BaseModel):
    """Analyze and route it according to its content."""
    chain_of_thought: str = Field(description="Reasoning about which agent need to handle the user query")
    router: Literal["company_info_agent", "delivery_agent", "order_agent", "transaction_agent"] = Field(description="transfor query to one of the sub-agents")

    


class State(MessagesState):
    # This state class has the messages key build in
    router: Literal["company_info_agent", "delivery_agent", "order_agent", "transaction_agent"] 
    

