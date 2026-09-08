import json
import os

TODO_FILE = "tasks.json"

if os.path.exists(TODO_FILE):
    with open(TODO_FILE, "r") as file:
        tasks = json.load(file)
else:
    tasks = []


def save_tasks():
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


user_input = (
    input("Enter command (add, list, update, delete, complete): ").strip().lower()
)


if user_input == "add":
    title = input("Enter task title: ")

    new_task = {"id": len(tasks) + 1, "title": title, "status": "not started"}

    tasks.append(new_task)
    save_tasks()

    print(f"Added: '{title}'")

elif user_input == "list":
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n ---List of Tasks---")

        for task in tasks:
            if task["status"] == "done":
                status = "[X]"
            elif task["status"] == "in progress":
                status = "[-]"
            else:
                status = "[ ]"
            print(f"{task['id']}. {status} {task['title']}")

elif user_input == "update":
    task_id = int(input("Enter task ID to update "))

    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter a new title: ")

            task["title"] = new_title
            save_tasks()

            print("Task updated successfully")
            break
        else:
            print("Task ID not found.")


elif user_input == "complete":
    task_id = int(input("Enter task ID to mark done: "))

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks()

            print(f"Marked '{task['title']}' as done")
            break
        else:
            print("Task ID not found")

elif user_input == "in progress":
    task_id = int(input("Enter task ID to mark in progress: "))

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in progress"
            save_tasks()

            print(f"Marked '{task['title']}' as in progress")
            break
        else:
            print("Task ID not found")

elif user_input == "delete":
    task_id = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks()

            print("Deleted successfully.")
            break
        else:
            print("Task id not found.")
