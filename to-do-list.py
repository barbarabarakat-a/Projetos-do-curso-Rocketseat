tasks = []

while True:
    print("\n==== To-Do List ====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks):
                status = "X" if t["done"] else "*"
                print(f"{i + 1}. {status} {t['task']}")

    elif choice == "3":
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")
