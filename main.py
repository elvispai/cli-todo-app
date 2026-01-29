# ------------------------------
# CLI To-Do App with File Saving
# ------------------------------

tasks = []

# Load tasks from file at start


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_text, done = line.strip().split(" | ")
                task = {
                    "task": task_text,
                    "done": True if done == "1" else False
                }
                tasks.append(task)
    except FileNotFoundError:
        # if file doesn't exit
        pass

# Save tasks to file


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            done = "Done" if task["done"] else "Undone"
            file.write(f"{task['task']} | {done}\n")


def show_menu():

    print("\n---To Do App---")
    print("1. View tasks.")
    print("2. Add task.")
    print("3. Mark tasks are done!")
    print("4. Delete tasks.")
    print("5. Exit.")

    choice = input("Choose an option(1 / 5): ")
    return choice


def view_tasks():

    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\nYour tasks: ")

    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❎"

        print(f"{index}. [{status}] {task['task']}")


def add_task():

    task_text = input("Enter the new task: ")

    task = {
        "task": task_text,
        "done": False
    }

    tasks.append(task)
    save_tasks()
    print("Task added Successfully.")


def mark_task_done():

    if not tasks:
        print("\nNo tasks to update.")
        return

    view_tasks()

    task_number = int(input("Enter the number to mask as done: "))

    if task_number < 1 or task_number > len(tasks):
        print("Invalid number")
        return

    tasks[task_number - 1]["done"] = True
    save_tasks()
    print(f"No.{task_number} marks as done.")


def deleted_task():

    if not tasks:
        print("\nNo tasks to update.")
        return

    view_tasks()

    task_number = int(input("Enter the number to delete the task: "))

    if task_number < 1 or task_number > len(tasks):
        print("Invalid number")
        return

    deleted_task = tasks.pop(task_number - 1)
    save_tasks()

    print(f"Now we delete the task: {deleted_task['task']}")


while True:

    user_choice = show_menu()
    if user_choice == "1":
        view_tasks()
    elif user_choice == "2":
        add_task()
    elif user_choice == "3":
        mark_task_done()
    elif user_choice == "4":
        deleted_task()
    elif user_choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid input.")
