
tasks = []

def show_tasks():
    print("\n--- YOUR TASKS ---")

    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['name']} - {status}")


while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        name = input("Enter task name: ").strip()

        if name:
            tasks.append({"name": name, "completed": False})
            print("Task added successfully!")
        else:
            print("Task name cannot be empty.")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()

        if tasks:
            try:
                number = int(input("Enter task number to complete: "))

                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        show_tasks()

        if tasks:
            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f"Deleted: {removed['name']}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please select 1-5.")
