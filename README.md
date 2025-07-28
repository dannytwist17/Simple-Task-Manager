# Simple-Task-Manager
A simple Python CLI app to manage tasks with add, view, update and delete.

# Simple Task Manager 📝

A simple command-line task manager built in Python. It lets you add, view, mark as done, delete, and save your daily tasks — all saved in a local JSON file for easy tracking.

---

## 📦 Features
- ✅ Add new tasks with a title and description
- 📋 View all saved tasks
- ✔️ Mark tasks as completed
- ❌ Delete tasks
- 💾 Auto-save to `tasks.json` (local file)
- 🔁 Keeps running until you choose to exit

---

## 🧠 How to Use

1. **Run the script** in your Python environment (e.g., Pydroid).
2. **Choose an option** from the menu:
   - `1` → Add Task  
   - `2` → View Tasks  
   - `3` → Mark Task as Done  
   - `4` → Delete Task  
   - `5` → Save and Exit  
   - `6` → Exit without saving
3. Your tasks are stored in a JSON file for later access.

---

## 💡 Requirements
- Python 3.x  
(No external libraries needed)

---

## 📁 File Structure
```bash
📦 simple-task-manager/
 ┣ 📄 DannyToDolist.py      # Main Python script
 ┗ 📄 tasks.json           # Auto-generated when saving tasks