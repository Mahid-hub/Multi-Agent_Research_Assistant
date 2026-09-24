from typing import TypedDict
from pydantic import BaseModel


class ResearchState(TypedDict):
    question: str
    tasks: list[str]
    search_result: list
    
class ResearchTasks(BaseModel):
    tasks: list[str]