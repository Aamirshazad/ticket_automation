from pydantic import BaseModel, Field
from typing_extensions import TypedDict, Literal
from langgraph.graph import MessagesState



class RouterSchema(BaseModel):
    """Analyze and route it according to its content."""
    pass

    


class StateInput(TypedDict):
    # This is the input to the state
    pass

class State(MessagesState):
    # This state class has the messages key build in
    pass

class UserPreferences(BaseModel):
    """Updated user preferences based on user's feedback."""
    chain_of_thought: str = Field(description="Reasoning about which user preferences need to add/update if required")
    user_preferences: str = Field(description="Updated user preferences")