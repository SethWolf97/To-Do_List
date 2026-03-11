# todo.py
# by Seth Wolf
# March 9th, 2026
# Fills in a to-do list

tasks = []

while True:
    command = input("Give a command (add/list/quit): ")
    if command.lower() == "quit":
        with open("list.txt", "w") as f:
            for i, task in enumerate(tasks):
                f.write(f"{i+1}. {task}\n")
        print("\nGoodbye")
        break
    elif command.lower() == "add":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif command.lower() == "list":
        print("\nTo-Do List")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print()
    else:
        print("Unknown command.")