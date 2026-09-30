from src.graph import graph

question = input("Enter your research question: ")

initial_state = {
    "question": question,
    "tasks": [],
    "search_result": [],
    "reader_results": [],
    "final_report": ""
}

final_state = graph.invoke(initial_state)       

# print("\nReader Results:")
# for item in final_state["reader_results"]:
#     print('-'*100)
#     print("\nTitle:", item["title"])
#     print("URL:", item["url"])
#     print("Summary:", item["summary"])
#     print("Question: ", final_state['question'])
#     print("Task: ", final_state['tasks'])
#     print("Search Result: ", final_state['search_result'])
#     print("Read Result: ", final_state['reader_results'])
#     print('-'*100)

print("FINAL RESULT: ", final_state['final_report'])