from langgraph.graph import StateGraph, START, END
from src.state import ResearchState
from Agents.orchestrator import orchestrator
from Agents.searcher import search_web
from Agents.reader import reader
from src.synthesizer import synthesize_report

builder = StateGraph(ResearchState)

builder.add_node("orchestrator", orchestrator)
builder.add_node("search_agent", search_web)
builder.add_node("reader_agent", reader)
builder.add_node("synthesize", synthesize_report)

builder.add_edge(START, "orchestrator")
builder.add_edge("orchestrator", "search_agent")
builder.add_edge("search_agent", "reader_agent")
builder.add_edge("reader_agent", "synthesize")
builder.add_edge("synthesize", END)

graph = builder.compile()
