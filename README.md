# Task manager

A to-do list for the terminal that remembers your tasks after you close it. Tasks are saved
to `tasks.json` after every change and loaded when the program starts.

## How to run it

You need Python 3.10 or newer. No extra packages are needed.

```
python tasks.py
```

Sample run:

```
1) Add  2) List  3) Done  4) Delete  5) Quit
Choose: 1
Task: Buy milk
Added task 1.
Choose: 1
Task: Read a book
Added task 2.
Choose: 3
Task number: 9
There is no task 9.
Choose: 3
Task number: abc
'abc' is not a number.
Choose: 3
Task number: 1
Task 1 marked as done.
Choose: 2
1. [x] Buy milk
2. [ ] Read a book
Choose: 4
Task number: 1
Deleted 'Buy milk'.
Choose: 2
1. [ ] Read a book
Choose: 5
Bye!
```

## What happens with wrong input

- A menu choice other than 1 to 5 prints `Please choose 1 to 5.`
- Letters or a number that is not a task print a message and go back to the menu.
- If `tasks.json` is missing, the program starts with an empty list. If it is broken (for
  example it contains `{oops`), it prints a warning and starts with an empty list.

## How the code is organised

All the code is in `tasks.py`. Each action has its own small function: `load_tasks`,
`save_tasks`, `add_task`, `complete_task`, `delete_task`, `show_tasks` and
`ask_task_number`. `main` only shows the menu and calls them.

## Tests

```
python -m unittest test_tasks.py
```
