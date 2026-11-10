# Task manager

A small command line program to add, list, complete and delete tasks. Tasks are saved in
`tasks.json`, so they are still there after you close the program.

## How to run it

You need Python 3.10 or newer. No extra packages are needed.

```
python tasks.py add "Buy milk"
python tasks.py add "Finish the Python project"
python tasks.py list
python tasks.py done 1
python tasks.py delete 2
```

Example output of `list`:

```
[x] 1: Buy milk
[ ] 2: Finish the Python project
```

## What happens with wrong input

- `python tasks.py done abc` prints `Error: 'abc' is not a number...` instead of crashing.
- An id that does not exist prints `Error: There is no task with id 9.`
- If `tasks.json` is missing, the program starts with an empty list. If it is broken,
  it prints a warning and starts with an empty list.

## Tests

```
python -m unittest test_tasks.py
```

## How the code is organised

All the code is in `tasks.py`. Each action has its own small function (`add_task`,
`complete_task`, `delete_task`, `load_tasks`, `save_tasks`), and `main` only reads the
command and calls them.
