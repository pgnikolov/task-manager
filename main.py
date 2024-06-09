import json
from datetime import datetime


def add_task(tasks, task):
    """
    Adds a new task to the task list.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task (dict): The task to be added.

    Returns:
    list of dict: Updated tasks.json.
    """

    tasks.append(task)
    return tasks


def remove_task(tasks, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated tasks.json.
    """
    task_to_remove = [task for task in tasks if task["id"] == task_id]
    if not task_to_remove:
        print(f"Task with ID {task_id} not found.")
        main()

    tasks.remove(task_to_remove[0])
    return tasks


def update_task(tasks, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated tasks.json.
    """
    task_to_update = [tasks.index(task) for task in tasks if task["id"] == task_id]
    if not task_to_update:
        print(f"Task with ID {task_id} not found.")
        main()

    tasks[task_to_update[0]].update(updated_task)

    return tasks


def get_task(tasks, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be retrieved.
    Returns:
        task info as dictionary
    """
    task_get = [tasks.index(task) for task in tasks if task["id"] == task_id]
    if not task_get:
        print(f"Task with ID {task_id} not found.")
        main()

    return tasks[task_get[0]]


def set_task_priority(tasks, task_id, priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be updated.
    priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    task_priority = [tasks.index(task) for task in tasks if task["id"] == task_id]
    if not task_priority:
        print(f"Task with ID {task_id} not found.")
        main()

    tasks[task_priority[0]]["priority"] = priority

    return tasks


def set_task_deadline(tasks, task_id, deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be updated.
    deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    task_deadline = [tasks.index(task) for task in tasks if task["id"] == task_id]
    if not task_deadline:
        print(f"Task with ID {task_id} not found.")
        main()

    tasks[task_deadline[0]]["deadline"] = deadline

    return tasks


def mark_task_as_completed(tasks, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    task_complete = [tasks.index(task) for task in tasks if task["id"] == task_id]
    if not task_complete:
        print(f"Task with ID {task_id} not found.")
        main()

    tasks[task_complete[0]]["completed"] = True

    return tasks


def set_task_description(tasks, task_id, description):
    """
    Sets the description for a task.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be updated.
    description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    task_desciption = [tasks.index(task) for task in tasks if task["id"] == task_id]
    if not task_desciption:
        print(f"Task with ID {task_id} not found.")
        main()

    tasks[task_desciption[0]]["description"] = description

    return tasks


def search_tasks_by_keyword(tasks, keyword):
    """
    Searches tasks.json by a keyword in the description.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    """
    founded_tasks = []

    for task in tasks:
        if keyword.lower() in task.get("description", "").lower():
            founded_tasks.append(task)

    if not founded_tasks:
        print(f"There is no task with '{keyword}' in description.")
        main()

    return founded_tasks


def filter_tasks_by_priority(tasks, priority):
    """
    Filters tasks.json by priority.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    """
    results_by_prio = []
    for task in tasks:
        if priority in task.get("priority", ""):
            results_by_prio.append(task)

    if not results_by_prio:
        print(f"There is no task with priority:'{priority}' in your tasks.")
        main()

    return results_by_prio


def filter_tasks_by_status(tasks, status):
    """
    Filters tasks.json by their completion status.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    status (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """
    results_by_status = []
    if status == "completed":
        status = True
    elif status == "pending":
        status = False

    for task in tasks:
        if task["completed"] == status:
            results_by_status.append(task)

    return results_by_status


def filter_tasks_by_deadline(tasks, deadline):
    """
    Filters tasks.json by their deadline.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    """
    results_by_deadline = []
    for task in tasks:
        if datetime.strptime(task["deadline"], '%d-%m-%Y') <= datetime.strptime(deadline, '%d-%m-%Y'):
            results_by_deadline.append(task)

    return results_by_deadline


def count_tasks(tasks):
    """
    Returns the total number of tasks.json.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    int: The total number of tasks.json.
    """
    return len(tasks)


def count_completed_tasks(tasks):
    """
    Returns the number of completed tasks.json.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    int: The number of completed tasks.json
    """

    status = True
    results_by_status = filter_tasks_by_status(tasks, status)

    return len(results_by_status)


def count_pending_tasks(tasks):
    """
    Returns the number of pending tasks.json.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    int: The number of pending tasks.json.
    """
    status = False
    results_by_status = filter_tasks_by_status(tasks, status)

    return len(results_by_status)


def generate_task_summary(tasks):
    """
    Generates a summary report of all tasks.json.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.json.
    """
    summary = {
        "Total pending tasks": count_pending_tasks(tasks),
        "Total completed tasks": count_completed_tasks(tasks)
    }
    return summary


def save_tasks_to_file(tasks, file_path):
    """
    Saves the task list to a file.

    Parameters:
    tasks (list of dict): The current list of tasks.
    file_path (str): The path to the file where tasks will be saved.
    Returns:
    None
    """
    try:
        f = open(file_path, 'r+')
        json.dump(tasks, f)
        f.close()
    except FileNotFoundError:
        print(f"The file path '{file_path}' does not exist.")


def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The path to the file where tasks are saved.

    Returns:
    list of dict: The loaded list of tasks.
    """
    try:
        f = open(file_path, "r")
        tasks = json.load(f)
        return tasks

    except FileNotFoundError:
        print(f"The file path -'{file_path}' does not exist.")


def sort_tasks_by_deadline(tasks):
    """
    Sorts tasks.json by their deadline.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    list of dict: The sorted list of tasks.json.
    """
    if not tasks:
        print("You have no tasks")
        main()

    tasks = sorted(tasks, key=lambda x: datetime.strptime(x["deadline"], '%d-%m-%Y'))

    return tasks


def sort_tasks_by_priority(tasks):
    """
    Sorts tasks.json by their priority.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    list of dict: The sorted list of tasks.json.
    """
    if not tasks:
        print("You have no tasks")
        main()

    priority_as_value = {"high": 1, "medium": 2, "low": 3}
    tasks = sorted(tasks, key=lambda x: priority_as_value[x["priority"]])

    return tasks


def id_validation(task_id):
    """
    Validate user id input as innteger.
    Args:
        task_id: The user id.
    Returns:
        task_id(int): After validation.
    """
    if type(task_id) is not int:
        while True:
            try:
                task_id = int(input("Enter a task ID: "))
                break
            except ValueError:
                print("Invalid input. Task ID must be an integer.")

    return task_id


def description_validation(description):
    """
    Validate user description input is not empty string.
    Args:
        description (str): The user description.
    Returns:
        description(str): After confirmation it is not an empty string.
    """
    if not description:
        print("Description can't be empty.")
        while True:
            description = input("Enter a task description: ").capitalize()
            if description:
                break
            else:
                print("Invalid input. Task description can't be empty.")
    return description


def priority_validation(priority):
    """
    Validate user priority input to be one of low, medium or high.
    Args:
        priority (str): The priority to validate.
    Returns:
        priority(str): After confirmation.
    """
    if priority not in ["low", "medium", "high"]:
        print("Your choice must be one of low, medium or high.")
        while True:
            priority = input("Enter task priority (low, medium, high): ").lower()
            if priority in ["low", "medium", "high"]:
                break
            else:
                print("Invalid input. Task priority must be 'low', 'medium' or 'high'.")

    return priority


def deadline_validation(deadline):
    """
    Validate the date format YYYY-MM-DD and check if it's not earlier than today's date.
    Args:
        deadline (str): The deadline to validate.
    Returns:
        deadline(str): After confirmation.
    """
    while True:
        try:
            date = datetime.strptime(deadline, '%d-%m-%Y')
            if date.date() >= datetime.today().date():
                break
            elif date.date() < datetime.today().date():
                print("Deadline can't be earlier than today's date.")
                deadline = input("Enter deadline (DD-MM-YYYY): ")
        except ValueError:
            print("Invalid date format. Please enter date in format DD-MM-YYYY.")
            deadline = input("Enter deadline in format (DD-MM-YYYY): ")

    deadline = date.strftime('%d-%m-%Y')
    return deadline


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
                    'id': id_validation(task_id=int(input("Enter task ID: "))),
                    'description': description_validation(description=input("Enter task description: ").capitalize()),
                    'priority': priority_validation(priority=input("Enter task priority (low, medium, high): ").lower()),
                    'deadline': deadline_validation(deadline=input("Enter deadline (DD-MM-YYYY): ")),
                    'completed': False
                }
                tasks = add_task(tasks, task)
                print("Task added successfully.")
            except ValueError:
                print("ID must be integer")
        elif choice == '2':
            task_id = id_validation(int(input("Enter task ID to remove: ")))
            tasks = remove_task(tasks, task_id)
            print("Task removed successfully.")
        elif choice == '3':
            task_id = id_validation(int(input("Enter task ID to update: ")))
            updated_task = {'description': description_validation(input("Enter new task description: ").capitalize()),
                            'priority': priority_validation(input("Enter new priority (low, medium, high): ").lower()),
                            'deadline': deadline_validation(input("Enter new task deadline (DD-MM-YYYY): "))}
            tasks = update_task(tasks, task_id, updated_task)
            print("Task updated successfully.")
        elif choice == '4':
            task_id = id_validation(int(input("Enter task ID to get: ")))
            task = get_task(tasks, task_id)
            print("Task details:", task)
        elif choice == '5':
            task_id = id_validation(int(input("Enter task ID to set priority: ")))
            priority = priority_validation(input("Enter new priority (low, medium, high): ").lower())
            tasks = set_task_priority(tasks, task_id, priority)
            print("Task priority set successfully.")
        elif choice == '6':
            task_id = id_validation(int(input("Enter task ID to set deadline: ")))
            deadline = deadline_validation(input("Enter new deadline (DD-MM-YYYY): "))
            tasks = set_task_deadline(tasks, task_id, deadline)
            print("Task deadline set successfully.")
        elif choice == '7':
            task_id = id_validation(int(input("Enter task ID to mark as completed: ")))
            tasks = mark_task_as_completed(tasks, task_id)
            print("Task marked as completed.")
        elif choice == '8':
            task_id = id_validation(int(input("Enter task ID to set description: ")))
            description = description_validation(input("Enter new description: ").capitalize())
            tasks = set_task_description(tasks, task_id, description)
            print("Task description set successfully.")
        elif choice == '9':
            keyword = input("Enter keyword to search: ").lower()
            found_tasks = search_tasks_by_keyword(tasks, keyword)
            print("Tasks found:", found_tasks)
        elif choice == '10':
            priority = priority_validation(input("Enter priority to filter by (low, medium, high): "))
            filtered_tasks = filter_tasks_by_priority(tasks, priority)
            print("Filtered tasks.json:", filtered_tasks)
        elif choice == '11':
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
            filtered_tasks = filter_tasks_by_status(tasks, status)
            print("Filtered tasks.json:", filtered_tasks)
        elif choice == '12':
            deadline = deadline_validation(input("Enter deadline to filter by (DD-MM-YYYY): "))
            filtered_tasks = filter_tasks_by_deadline(tasks, deadline)
            print("Filtered tasks.json:", filtered_tasks)
        elif choice == '13':
            total_tasks = count_tasks(tasks)
            print("Total number of tasks.json:", total_tasks)
        elif choice == '14':
            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks.json:", completed_tasks)
        elif choice == '15':
            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks.json:", pending_tasks)
        elif choice == '16':
            summary = generate_task_summary(tasks)
            print("Task Summary:", summary)
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
