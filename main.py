from src.graph import graph

question = input("Enter your research question: ")

initial_state = {
    "question": question,
    "tasks": []
}

final_state = graph.invoke(initial_state)

print("\nResult:")

for i, task in enumerate(final_state["tasks"], start=1):
        print(f"{i}. {task}")