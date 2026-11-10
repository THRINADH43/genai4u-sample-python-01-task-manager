"""A small command line task manager. Tasks are kept in tasks.json next to this file."""

import json
import os

TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks(path=TASKS_FILE):
    """Read the task list from the JSON file. A missing or broken file gives an empty list."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            tasks = json.load(f)
    except json.JSONDecodeError:
        print(f"Warning: {path} is broken (not valid JSON), starting with an empty list.")
        return []
    if not isinstance(tasks, list):
        print(f"Warning: {path} does not hold a list of tasks, starting with an empty list.")
        return []
    return tasks


def save_tasks(tasks, path=TASKS_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("A task needs a title.")
    task = {"title": title, "done": False}
    tasks.append(task)
    return task


def check_index(tasks, index):
    if not 0 <= index < len(tasks):
        raise ValueError(f"There is no task {index + 1}.")


def complete_task(tasks, index):
    check_index(tasks, index)
    tasks[index]["done"] = True


def delete_task(tasks, index):
    check_index(tasks, index)
    return tasks.pop(index)


def format_task(number, task):
    mark = "x" if task["done"] else " "
    return f"{number}. [{mark}] {task['title']}"


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for number, task in enumerate(tasks, start=1):
        print(format_task(number, task))


def ask_task_number(tasks):
    """Ask for a task number as shown by the list (from 1). Returns the task's list index."""
    text = input("Task number: ").strip()
    try:
        number = int(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a number.")
    check_index(tasks, number - 1)
    return number - 1


MENU = "1) Add  2) List  3) Done  4) Delete  5) Quit"


def main():
    tasks = load_tasks()
    print(MENU)
    while True:
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                task = add_task(tasks, input("Task: "))
                save_tasks(tasks)
                print(f"Added task {len(tasks)}.")
            elif choice == "2":
                show_tasks(tasks)
            elif choice == "3":
                index = ask_task_number(tasks)
                complete_task(tasks, index)
                save_tasks(tasks)
                print(f"Task {index + 1} marked as done.")
            elif choice == "4":
                index = ask_task_number(tasks)
                removed = delete_task(tasks, index)
                save_tasks(tasks)
                print(f"Deleted '{removed['title']}'.")
            elif choice == "5":
                print("Bye!")
                return
            else:
                print("Please choose 1 to 5.")
        except ValueError as err:
            print(err)


if __name__ == "__main__":
    main()
