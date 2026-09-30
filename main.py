from src.graph import graph

question = input("Enter your research question: ")

initial_state = {
    "question": question,
    "tasks": [],
    "search_result": [],
    "reader_results": []
}

final_state = graph.invoke(initial_state)

# print("\nResult:")

# for i, task in enumerate(final_state["tasks"], start=1):
#         print(f"{i}. {task}")
        
# print(final_state['search_result'])        

print("\nReader Results:")

for item in final_state["reader_results"]:
    print("\nTitle:", item["title"])
    print("URL:", item["url"])
    print("Summary:", item["summary"])