import json
import os

FILENAME = 'todo_list.json'
print("JSON file path:", os.path.abspath(FILENAME))

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved successfully!")

def add_tasks(tasks):
    description = input('Enter task description: ')
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    due_date = due_date if due_date else None
    priority = input("Enter priority (High / Medium / Low) or leave blank: ").strip()
    priority = priority if priority else "None"
    task = {
        'description': description,
        'done': False,
        'due_date': due_date,
        'priority': priority
    }
    tasks.append(task)
    save_tasks(tasks)
    print('Task Added!')

def view_tasks(tasks):
    if not tasks:
        print('No tasks yet.')
        return

    undone_tasks = [t for t in tasks if not t['done']]
    done_tasks = [t for t in tasks if t['done']]

    if undone_tasks:
        print("\n--- Tasks To Do ---")
        for i, task in enumerate(undone_tasks, 1):
            due = f"(Due: {task['due_date']})" if task.get('due_date') else ""
            priority = f"[priority: {task.get('priority', 'None')}]"
            print(f"{i}. {task['description']} [❌] {due} {priority}")
    else:
        print("\nNo tasks pending!")

    if done_tasks:
        print("\n--- Completed Tasks ---")
        for i, task in enumerate(done_tasks, 1):
            due = f"(Due: {task['due_date']})" if task.get('due_date') else ""
            priority = f"[priority: {task.get('priority', 'None')}]"
            print(f"{i}. {task['description']} [✅] {due} {priority}")
    else:
        print("\nNo tasks completed yet.")

def mark_done(tasks):
    undone_tasks = [t for t in tasks if not t['done']]

    if not undone_tasks:
        print("No pending tasks to mark as done.")
        return

    print("\n--- Tasks To Do ---")
    for i, task in enumerate(undone_tasks, 1):
        due = f"(Due: {task['due_date']})" if task.get('due_date') else ""
        priority = f"[priority: {task.get('priority', 'None')}]"
        print(f"{i}. {task['description']} [❌] {due} {priority}")

    try:
        num = int(input('Enter task number to mark as done: '))
        if 1 <= num <= len(undone_tasks):
            selected_task = undone_tasks[num - 1]
            selected_task['done'] = True
            save_tasks(tasks)
            print('Task marked as done!')
        else:
            print('Invalid task number.')
    except ValueError:
        print('Invalid input.')

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    print("\n--- All Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "[✅]" if task['done'] else "[❌]"
        due = f"(Due: {task['due_date']})" if task.get('due_date') else ""
        priority = f"[priority: {task.get('priority', 'None')}]"
        print(f"{i}. {task['description']} {status} {due} {priority}")

    try:
        num = int(input('Enter task number to delete: '))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['description']}")
        else:
            print('Invalid task number.')
    except ValueError:
        print('Invalid input.')

def edit_task(tasks):
    if not tasks:
        print("No tasks to edit.")
        return

    print("\n--- All Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "[✅]" if task['done'] else "[❌]"
        due = f"(Due: {task['due_date']})" if task.get('due_date') else ""
        priority = f"[priority: {task.get('priority', 'None')}]"
        print(f"{i}. {task['description']} {status} {due} {priority}")

    try:
        num = int(input("Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            task = tasks[num - 1]

            current_desc = task.get("description", "")
            current_due = task.get("due_date", "")
            current_priority = task.get("priority", "")

            print(f"\nCurrent description: {current_desc}")
            print(f"Current due date: {current_due if current_due else 'None'}")
            print(f"Current priority: {current_priority if current_priority else 'None'}")

            new_desc = input("Enter new description (leave blank to keep current): ").strip()
            new_due = input("Enter new due date (YYYY-MM-DD) or leave blank to keep current: ").strip()
            new_priority = input("Enter new priority (High / Medium / Low) or leave blank to keep current: ").strip()

            if new_desc:
                task['description'] = new_desc
            if new_due:
                task['due_date'] = new_due
            if new_priority:
                task['priority'] = new_priority

            save_tasks(tasks)
            print("Task Updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")
        
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Edit task")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()