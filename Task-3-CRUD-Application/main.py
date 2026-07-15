tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            index = int(input("Enter task number to update: ")) - 1

            if 0 <= index < len(tasks):
                new_task = input("Enter new task: ")
                tasks[index] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            index = int(input("Enter task number to delete: ")) - 1

            if 0 <= index < len(tasks):
                deleted = tasks.pop(index)
                print(f"'{deleted}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
