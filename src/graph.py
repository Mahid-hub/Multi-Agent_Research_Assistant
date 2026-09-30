from langgraph.graph import StateGraph, START, END
from src.state import ResearchState
from Agents.orchestrator import orchestrator
from Agents.searcher import search_web
from Agents.Reader import reader

builder = StateGraph(ResearchState)

builder.add_node("orchestrator", orchestrator)
builder.add_node("search_agent", search_web)
builder.add_node("reader_agent", reader)

builder.add_edge(START, "orchestrator")
builder.add_edge("orchestrator", "search_agent")
builder.add_edge("search_agent", "reader_agent")
builder.add_edge("reader_agent", END)

graph = builder.compile()
