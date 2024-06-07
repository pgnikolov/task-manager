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
	existing_ids = [t["id"] for t in tasks]

	if task["id"] in existing_ids:
		return f"You already have task with ID {task['id']}!"

	tasks.append(task)
	with open('tasks.json', 'w') as f:
		json.dump(tasks, f,)
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
	tasks.remove(task_to_remove)

	with open('tasks.json', 'w') as f:
		json.dump(tasks, f)
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
	for task in tasks:
		if task["id"] == task_id:
			task.update(updated_task)
			break
	with open('tasks.json', 'w') as f:
		json.dump(tasks, f)

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
	task_to_get = [task for task in tasks if task["id"] == task_id]

	return task_to_get


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
	for task in tasks:
		if task["id"] == task_id:
			task['priority'] = priority
			break

	with open('tasks.json', 'w') as f:
		json.dump(tasks, f)
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
	for task in tasks:
		if task['id'] == task_id:
			task['deadline'] = deadline
			break

	with open('tasks.json', 'w') as f:
		json.dump(tasks, f)
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
	for task in tasks:
		if task['id'] == task_id:
			task['completed'] = True
			break
	with open('tasks.json', 'w') as f:
		json.dump(tasks, f)
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
	for task in tasks:
		if task['id'] == task_id:
			task['description'] = description
			break
	with open('tasks.json', 'w') as f:
		json.dump(tasks, f)
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
		if keyword in task.get("description", ""):
			founded_tasks.append(task)

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
		if datetime.strptime(task["deadline"], '%Y-%m-%d') <= datetime.strptime(deadline, '%Y-%m-%d'):
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


def sort_tasks_by_deadline(tasks):
	"""
	Sorts tasks.json by their deadline.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.

	Returns:
	list of dict: The sorted list of tasks.json.
	"""
	tasks = sorted(tasks, key=lambda x: datetime.strptime(x["deadline"], '%Y-%m-%d'))
	with open('tasks.json', 'w') as f:
		json.dump(tasks, f)
	return tasks


def sort_tasks_by_priority(tasks):
	"""
	Sorts tasks.json by their priority.

	Parameters:
	tasks.json (list of dict): The current list of tasks.json.

	Returns:
	list of dict: The sorted list of tasks.json.
	"""
	priority_as_value = {"high": 1, "medium": 2, "low": 3}
	tasks = sorted(tasks, key=lambda x: priority_as_value[x["priority"]])
	with open('tasks.json', 'w') as f:
		json.dump(tasks, f)
	return tasks


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
	17. Sort Tasks by Deadline
	18. Sort Tasks by Priority
	19. Exit
	"""
	print(menu)


def main():
	with open('tasks.json', 'r') as f:
		tasks = json.load(f)
	while True:
		print_menu()
		choice = input("Enter your choice: ")
		if choice == '1':
			task = {
				'id': int(input("Enter task ID: ")),
				'description': input("Enter task description: "),
				'priority': input("Enter task priority (low, medium, high): "),
				'deadline': input("Enter task deadline (YYYY-MM-DD): "),
				'completed': False
			}
			tasks = add_task(tasks, task)
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
			tasks = sort_tasks_by_deadline(tasks)
			print("Tasks sorted by deadline.")
		elif choice == '18':
			tasks = sort_tasks_by_priority(tasks)
			print("Tasks sorted by priority.")
		elif choice == '19':
			print("Exiting...")
			break
		else:
			print("Invalid choice. Please try again.")


if __name__ == "__main__":
	main()
