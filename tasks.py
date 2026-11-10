"""A small command line task manager. Tasks are kept in tasks.json next to this file."""

import json
import os
import sys

TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks(path=TASKS_FILE):
    """Read the task list from the JSON file. A missing or broken file gives an empty list."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            tasks = json.load(f)
    except json.JSONDecodeError:
        print(f"Warning: {path} is not valid JSON, starting with an empty list.")
        return []
    if not isinstance(tasks, list):
        print(f"Warning: {path} does not hold a list of tasks, starting with an empty list.")
        return []
    return tasks


def save_tasks(tasks, path=TASKS_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("A task needs a title.")
    task = {"id": next_id(tasks), "title": title, "done": False}
    tasks.append(task)
    return task


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise ValueError(f"There is no task with id {task_id}.")


def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    task["done"] = True
    return task


def delete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    tasks.remove(task)
    return task


def format_task(task):
    mark = "x" if task["done"] else " "
    return f"[{mark}] {task['id']}: {task['title']}"


def parse_id(text):
    try:
        return int(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a number. Use the task id shown by 'list'.")


USAGE = """Usage:
  python tasks.py add "Buy milk"
  python tasks.py list
  python tasks.py done 2
  python tasks.py delete 2"""


def main(argv):
    if not argv:
        print(USAGE)
        return 1
    command, args = argv[0], argv[1:]
    tasks = load_tasks()
    try:
        if command == "add":
            if not args:
                raise ValueError("Give the task title, for example: add \"Buy milk\"")
            task = add_task(tasks, " ".join(args))
            save_tasks(tasks)
            print(f"Added task {task['id']}.")
        elif command == "list":
            if not tasks:
                print("No tasks yet.")
            for task in tasks:
                print(format_task(task))
        elif command in ("done", "delete"):
            if len(args) != 1:
                raise ValueError(f"Give exactly one task id, for example: {command} 2")
            task_id = parse_id(args[0])
            if command == "done":
                complete_task(tasks, task_id)
                print(f"Task {task_id} marked as done.")
            else:
                delete_task(tasks, task_id)
                print(f"Task {task_id} deleted.")
            save_tasks(tasks)
        else:
            print(f"Unknown command '{command}'.")
            print(USAGE)
            return 1
    except ValueError as err:
        print(f"Error: {err}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
