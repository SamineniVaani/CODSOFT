import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({"task": task, "done": False})

def update_task(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        new_task = input("Enter the new task description: ")
        tasks[task_num]["task"] = new_task
    else:
        print("Invalid task number.")

def mark_task_done(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
    else:
        print("Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            mark_task_done(tasks)
            save_tasks(tasks)
        elif choice == "5":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
