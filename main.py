from langfuse import propagate_attributes
from src.graph import graph
from langfuse.langchain import CallbackHandler

langfuse_handler = CallbackHandler()

question = input("Enter your research question: ").strip()

if not question:
    print("Please enter a research question.")
    exit()

if len(question) < 5:
    print("Research question is too short.")
    exit()
    
initial_state = {
    "question": question,
    "tasks": [],
    "search_result": [],
    "reader_results": [],
    "final_report": ""
}

try:
    with propagate_attributes(
        trace_name="Multi-Agent Research Assistant",
        tags=["research", "multi-agent", "langgraph"],
        metadata={
            "project": "multi-agent-research",
            "framework": "LangGraph",
            "question": question
        }
    ):
        final_state = graph.invoke(
            initial_state,
            config={
                "callbacks": [langfuse_handler]
            }
        )

    print("\nFINAL RESULT:")
    print(final_state["final_report"])

except Exception as e:
    print("\nResearch workflow failed.")
    print(f"Error: {e}")