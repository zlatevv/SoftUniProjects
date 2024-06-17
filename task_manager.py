import json
from datetime import datetime


def add_task(tasks: list, task: dict) -> list:
    tasks.append(task)
    sorted_tasks = sorted(tasks, key=lambda x: x['id'])
    return sorted_tasks

def remove_task(tasks : list, task_id: int) -> list:
    tasks = [task for task in tasks if task['id'] != task_id]
    return tasks


def update_task(tasks: list, task_id: int, updated_task: dict)-> list:
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task)
    return tasks


def get_task(tasks: list, task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
        return "No such task found."


def set_task_priority(tasks: list, task_id: int, priority: str)-> str:
    for task in tasks:
        if task['id'] == task_id:
            task['priority'] = priority
    return f"New priority set to {priority}"


def set_task_deadline(tasks:list, task_id:int, deadline:str)-> str:
    for task in tasks:
        if task['id'] == task_id:
            task['deadline'] = deadline
    return f"New deadline set to {deadline}"


def mark_task_as_completed(tasks:list, task_id:int)-> list:
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
    return tasks


def set_task_description(tasks: list, task_id:int, description:str)-> list:
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
    return tasks


def search_tasks_by_keyword(tasks:list, keyword:str):
    return [task for task in tasks if keyword in task['description']]

def filter_tasks_by_priority(tasks:list, priority:str)->list:
    return [task for task in tasks if task['priority'] == priority]
            


def filter_tasks_by_status(tasks:list, status:bool)-> list:
    return [task for task in tasks if task.get('completed') == status]


def filter_tasks_by_deadline(tasks:list, deadline:str):
    return [task for task in tasks if task['deadline'] == deadline]


def count_tasks(tasks:list)-> int:
    return len(tasks)

def count_completed_tasks(tasks:list)-> int:
    completed = []
    for task in tasks:
        if task['completed'] == True:
            completed.append(task)
    return len(completed)


def count_pending_tasks(tasks:list)-> int:
    pending = []
    for task in tasks:
        if task['completed'] == False:
            pending.append(task)
    return len(pending)

def generate_task_summary(tasks:list)-> str:
    completed = []
    pending = []
    total = []
    for task in tasks:
        if task['completed'] == True:
            completed.append(task)
            total.append(task)
        elif task['completed'] == False:
            pending.append(task)
            total.append(task)
    return f"Total tasks: {len(total)}\nCompleted tasks: {len(completed)}\nPending tasks: {len(pending)}"


def save_tasks_to_file(tasks:list, file_path:str):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent = 4)

def load_tasks_from_file(file_path:str):
    try:
        with open(file_path, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return "No such file"


def sort_tasks_by_deadline(tasks:list)-> list:
    sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x['deadline'], '%Y-%m-%d'))
    return sorted_tasks


def sort_tasks_by_priority(tasks:list)->list:
    priority_order = {"low": 0, "medium": 1, "high": 2}
    sorted_tasks = sorted(tasks, key=lambda task: priority_order.get(task['priority'], float('inf')))
    return sorted_tasks


def print_menu():
    """
    Prints the user menu.
    """
    menu = """
    Task Manager Menu:
    1. Add Task
    2. Remove Task
    3. Update Task
    4. Get Task
    5. Set Task Priority
    6. Set Task Deadline
    7. Mark Task as Completed
    8. Set Task Description
    9. Search Tasks by Keyword
    10. Filter Tasks by Priority
    11. Filter Tasks by Status
    12. Filter Tasks by Deadline
    13. Count Tasks
    14. Count Completed Tasks
    15. Count Pending Tasks
    16. Generate Task Summary
    17. Save Tasks to File
    18. Load Tasks from File
    19. Sort Tasks by Deadline
    20. Sort Tasks by Priority
    21. Exit
    """
    print(menu)


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                task = {
                    'id': int(input("Enter task ID: ")),
                    'description': input("Enter task description: "),
                    'priority': input("Enter task priority (low, medium, high): "),
                    'deadline': input("Enter task deadline (YYYY-MM-DD): "),
                    'completed': False
                }
                tasks = add_task(tasks, task)
                for t in tasks:
                    print(t)
                print("Task added successfully.")
            except ValueError:
                print("Invalid input")
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to remove: "))
                tasks = remove_task(tasks, task_id)
                print("Task removed successfully.")
            except ValueError:
                print("Invalid input")
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                updated_task = {
                    'description': input("Enter new task description: "),
                    'priority': input("Enter new task priority (low, medium, high): "),
                    'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
                }
                tasks = update_task(tasks, task_id, updated_task)
                print("Task updated successfully.")
            except ValueError:
                print("Invalid input")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to get: "))
                task = get_task(tasks, task_id)
                print("Task details:", task)
            except ValueError:
                print("Invalid input")
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to set priority: "))
                priority = input("Enter new priority (low, medium, high): ")
                tasks = set_task_priority(tasks, task_id, priority)
                print("Task priority set successfully.")
            except ValueError:
                print("Invalid input")
        elif choice == '6':
            try:
                task_id = int(input("Enter task ID to set deadline: "))
                deadline = input("Enter new deadline (YYYY-MM-DD): ")
                tasks = set_task_deadline(tasks, task_id, deadline)
                print("Task deadline set successfully.")
            except ValueError:
                print("Invalid input")
        elif choice == '7':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                tasks = mark_task_as_completed(tasks, task_id)
                print("Task marked as completed.")
            except ValueError:
                print("Invalid input")
        elif choice == '8':
            try:
                task_id = int(input("Enter task ID to set description: "))
                description = input("Enter new description: ")
                tasks = set_task_description(tasks, task_id, description)
                print("Task description set successfully.")
            except ValueError:
                print("Invalid input")
        elif choice == '9':
            keyword = input("Enter keyword to search: ")
            found_tasks = search_tasks_by_keyword(tasks, keyword)
            print("Tasks found:", found_tasks)
        elif choice == '10':
            priority = input("Enter priority to filter by (low, medium, high): ")
            filtered_tasks = filter_tasks_by_priority(tasks, priority)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '11':
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
            filtered_tasks = filter_tasks_by_status(tasks, status)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '12':
            deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")
            filtered_tasks = filter_tasks_by_deadline(tasks, deadline)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '13':
            total_tasks = count_tasks(tasks)
            print("Total number of tasks:", total_tasks)
        elif choice == '14':
            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks:", completed_tasks)
        elif choice == '15':
            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks:", pending_tasks)
        elif choice == '16':
            summary = generate_task_summary(tasks)
            print("Task Summary\n:", summary)
        elif choice == '17':
            file_path = input("Enter file path to save tasks: ")
            save_tasks_to_file(tasks, file_path)
            print("Tasks saved to file.")
        elif choice == '18':
            file_path = input("Enter file path to load tasks from: ")
            tasks = load_tasks_from_file(file_path)
            print("Tasks loaded from file.")
        elif choice == '19':
            tasks = sort_tasks_by_deadline(tasks)
            print("Tasks sorted by deadline.")
        elif choice == '20':
            tasks = sort_tasks_by_priority(tasks)
            print("Tasks sorted by priority.")
        elif choice == '21':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()