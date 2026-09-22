"""
Section 3: To-Do List Manager
Covers: Data Structure: List, Data Structure: Tuples
"""


class ToDoList:
    def __init__(self):
        # each task is stored as an immutable tuple: (task, priority, deadline)
        self.tasks = []  # list of tuples

    def add_task(self, task, priority="Medium", deadline="N/A"):
        self.tasks.append((task, priority, deadline))
        print(f"Added: {task} [{priority}] due {deadline}")

    def remove_task(self, index):
        try:
            removed = self.tasks.pop(index)
            print(f"Removed: {removed[0]}")
        except IndexError:
            print("No task at that position.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        sorted_tasks = sorted(
            self.tasks,
            key=lambda t: {"High": 0, "Medium": 1, "Low": 2}.get(t[1], 3),
        )
        print("\nYour tasks (sorted by priority):")
        for i, (task, priority, deadline) in enumerate(sorted_tasks):
            print(f"  {i}. [{priority}] {task} (due {deadline})")


def run_todo_menu():
    print("\n--- To-Do List Manager ---")
    todo = ToDoList()
    while True:
        print("\n1. Add task  2. Remove task  3. View tasks  4. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            task = input("Task: ")
            priority = input("Priority (High/Medium/Low): ") or "Medium"
            deadline = input("Deadline (e.g. 2026-09-30): ") or "N/A"
            todo.add_task(task, priority, deadline)
        elif choice == "2":
            todo.view_tasks()
            idx = input("Index to remove: ")
            if idx.isdigit():
                todo.remove_task(int(idx))
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            break
        else:
            print("Unknown option.")
