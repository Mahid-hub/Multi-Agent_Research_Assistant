from src.graph import graph
from langfuse.langchain import CallbackHandler

langfuse_handler = CallbackHandler()

question = input("Enter your research question: ").strip()

if not question:
    print("Error: Research question cannot be empty.")
    exit()
    
initial_state = {
    "question": question,
    "tasks": [],
    "search_result": [],
    "reader_results": [],
    "final_report": ""
}

final_state = graph.invoke(initial_state, config={"callbacks": [langfuse_handler]})       

if not final_state["final_report"]:
    print("Error: No final report was generated.")
    exit()
    
print("FINAL RESULT: ", final_state['final_report'])