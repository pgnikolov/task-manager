import json
from datetime import datetime


def add_task(tasks):
	"""
	Adds a new task to the task list.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	task (dict): The task to be added.

	Returns:
	list of dict: Updated list of tasks.json.
	"""
	task = {
		'id': int(input("Enter task ID: ")),
		'description': input("Enter task description: ").capitalize(),
		'priority': input("Enter task priority (low, medium, high): ").upper(),
		'deadline': input("Enter task deadline (YYYY-MM-DD): "),
		'completed': False
	}
	tasks[task["id"]] = task
	with open('tasks.json', 'w') as f:
		json.dump(tasks, f, indent=4)
	return tasks


def remove_task(tasks, task_id):
	"""
	Removes a task by its ID.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	task_id (int): The ID of the task to be removed.

	Returns:
	list of dict: Updated list of tasks.json.
	"""
	task_id = str(task_id)
	if task_id not in tasks:
		print(f"Task with with ID: {task_id} not found.")

	else:
		del tasks[task_id]

		with open('tasks.json', 'w') as f:
			json.dump(tasks, f, indent=4)


def update_task(tasks, task_id, updated_task):
	"""
	Updates an existing task.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	task_id (int): The ID of the task to be updated.
	updated_task (dict): The updated task details.

	Returns:
	list of dict: Updated list of tasks.json.
	"""


def get_task(tasks, task_id):
	"""
	Retrieves a task by its ID.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	task_id (int): The ID of the task to be retrieved.

	Returns:
	dict: The task with the specified ID, or None if not found.
	"""


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


def mark_task_as_completed(tasks, task_id):
	"""
	Marks a task as completed.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	task_id (int): The ID of the task to be marked as completed.

	Returns:
	list of dict: Updated list of tasks.json.
	"""


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


def search_tasks_by_keyword(tasks, keyword):
	"""
	Searches tasks.json by a keyword in the description.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	keyword (str): The keyword to search for.

	Returns:
	list of dict: Tasks that contain the keyword in their description.
	"""


def filter_tasks_by_priority(tasks, priority):
	"""
	Filters tasks.json by priority.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	priority (str): The priority level to filter by.

	Returns:
	list of dict: Tasks with the specified priority.
	"""


def filter_tasks_by_status(tasks, status):
	"""
	Filters tasks.json by their completion status.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	status (bool): The completion status to filter by.

	Returns:
	list of dict: Tasks with the specified completion status.
	"""


def filter_tasks_by_deadline(tasks, deadline):
	"""
	Filters tasks.json by their deadline.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	deadline (str): The deadline to filter by.

	Returns:
	list of dict: Tasks with the specified deadline.
	"""


def count_tasks(tasks):
	"""
	Returns the total number of tasks.json.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.

	Returns:
	int: The total number of tasks.json.
	"""


def count_completed_tasks(tasks):
	"""
	Returns the number of completed tasks.json.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.

	Returns:
	int: The number of completed tasks.json.
	"""


def count_pending_tasks(tasks):
	"""
	Returns the number of pending tasks.json.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.

	Returns:
	int: The number of pending tasks.json.
	"""


def generate_task_summary(tasks):
	"""
	Generates a summary report of all tasks.json.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.

	Returns:
	dict: A summary report containing total, completed, and pending tasks.json.
	"""


def save_tasks_to_file(tasks, file_path):
	"""
	Saves the task list to a file.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.
	file_path (str): The path to the file where tasks.json will be saved.

	Returns:
	None
	"""


def load_tasks_from_file(file_path):
	"""
	Loads the task list from a file.

	Parameters:
	file_path (str): The path to the file where tasks.json are saved.

	Returns:
	list of dict: The loaded list of tasks.json.
	"""


def sort_tasks_by_deadline(tasks):
	"""
	Sorts tasks.json by their deadline.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.

	Returns:
	list of dict: The sorted list of tasks.json.
	"""


def sort_tasks_by_priority(tasks):
	"""
	Sorts tasks.json by their priority.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.

	Returns:
	list of dict: The sorted list of tasks.json.
	"""


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
	with open('tasks.json', 'r') as f:
		tasks = json.load(f)
	while True:
		print_menu()
		choice = input("Enter your choice: ")
		if choice == '1':
			add_task(tasks)
			print("Task added successfully.")
		elif choice == '2':
			task_id = int(input("Enter task ID to remove: "))
			tasks = remove_task(tasks, task_id)
			print("Task removed successfully.")
		elif choice == '3':
			task_id = int(input("Enter task ID to update: "))
			updated_task = {
				'description': input("Enter new task description: "),
				'priority': input("Enter new task priority (low, medium, high): "),
				'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
			}
			tasks = update_task(tasks, task_id, updated_task)
			print("Task updated successfully.")
		elif choice == '4':
			task_id = int(input("Enter task ID to get: "))
			task = get_task(tasks, task_id)
			print("Task details:", task)
		elif choice == '5':
			task_id = int(input("Enter task ID to set priority: "))
			priority = input("Enter new priority (low, medium, high): ")
			tasks = set_task_priority(tasks, task_id, priority)
			print("Task priority set successfully.")
		elif choice == '6':
			task_id = int(input("Enter task ID to set deadline: "))
			deadline = input("Enter new deadline (YYYY-MM-DD): ")
			tasks = set_task_deadline(tasks, task_id, deadline)
			print("Task deadline set successfully.")
		elif choice == '7':
			task_id = int(input("Enter task ID to mark as completed: "))
			tasks = mark_task_as_completed(tasks, task_id)
			print("Task marked as completed.")
		elif choice == '8':
			task_id = int(input("Enter task ID to set description: "))
			description = input("Enter new description: ")
			tasks = set_task_description(tasks, task_id, description)
			print("Task description set successfully.")
		elif choice == '9':
			keyword = input("Enter keyword to search: ")
			found_tasks = search_tasks_by_keyword(tasks, keyword)
			print("Tasks found:", found_tasks)
		elif choice == '10':
			priority = input("Enter priority to filter by (low, medium, high): ")
			filtered_tasks = filter_tasks_by_priority(tasks, priority)
			print("Filtered tasks.json:", filtered_tasks)
		elif choice == '11':
			status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
			filtered_tasks = filter_tasks_by_status(tasks, status)
			print("Filtered tasks.json:", filtered_tasks)
		elif choice == '12':
			deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")
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
			file_path = input("Enter file path to save tasks.json: ")
			save_tasks_to_file(tasks, file_path)
			print("Tasks saved to file.")
		elif choice == '18':
			file_path = input("Enter file path to load tasks.json from: ")
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
