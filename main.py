from src.graph import graph
from langfuse.langchain import CallbackHandler

langfuse_handler = CallbackHandler()

question = input("Enter your research question: ")

initial_state = {
    "question": question,
    "tasks": [],
    "search_result": [],
    "reader_results": [],
    "final_report": ""
}

final_state = graph.invoke(initial_state, config={"callbacks": [langfuse_handler]})       

print("FINAL RESULT: ", final_state['final_report'])