# todo.py
# by Seth Wolf
# March 9th, 2026
# Fills in a to-do list

tasks = [] # list to fill with tasks

while True:
    command = input("Give a command (add/list/quit): ")
    match(command.lower()):
        case("quit"):
            with open("list.txt", "w") as f:
                for i, task in enumerate(tasks):
                    f.write(f"{i+1}. {task}\n")
            print("\nGoodbye")
            break
        case("add"):
            task = input("Enter a task: ")
            tasks.append(task)
        case("list"):
            print("\nTo-Do List")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            print()
        case _:
            print("Unknown command.")