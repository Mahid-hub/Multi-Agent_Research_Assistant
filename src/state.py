from typing import TypedDict
from pydantic import BaseModel


class ResearchState(TypedDict):
    question: str
    tasks: list[str]
    search_result: list
    reader_results: list
    final_report: str
    
class ResearchTasks(BaseModel):
    tasks: list[str]
    
class ReaderResult(BaseModel):
    summary: str

class FinalReport(BaseModel):
    report: str