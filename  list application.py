# Simple To-Do List Application

import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        show_tasks(tasks)
        print("\nOptions: [a]dd, [r]emove, [q]uit")
        choice = input("Choose an option: ").strip().lower()
        if choice == "a":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
        elif choice == "r":
            num = input("Enter task number to remove: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                    tasks.pop(idx)
                    save_tasks(tasks)
        elif choice == "q":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()