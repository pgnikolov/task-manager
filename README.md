# Task Manager :notebook:	

 <img src="https://github.com/pgnikolov/task-manager/assets/151896883/9324d27a-9ef9-4a0c-9e02-f74876ce36f9" width="1024" height="640">
 
A simple command-line task manager application written in Python. This project allows users to manage tasks by adding, updating, removing, and filtering tasks based on various criteria.

## Features

- Add Task: Add new tasks to the list.
- Remove Task: Remove tasks by their ID.
- Update Task: Update task details such as description, priority, and deadline.
- Get Task: Retrieve task details by their ID.
- Set Task Priority: Set the priority of a task.
- Set Task Deadline: Set the deadline for a task.
- Mark Task as Completed: Mark tasks as completed.
- Set Task Description: Set or update the description of a task.
- Search Tasks by Keyword: Search tasks by a keyword in their description.
- Filter Tasks by Priority: Filter tasks by their priority.
- Filter Tasks by Status: Filter tasks by their completion status (completed or pending).
- Filter Tasks by Deadline: Filter tasks by their deadline.
- Count Tasks: Get the total number of tasks.
- Count Completed Tasks: Get the number of completed tasks.
- Count Pending Tasks: Get the number of pending tasks.
- Generate Task Summary: Generate a summary report of all tasks.
- Sort Tasks by Deadline: Sort tasks by their deadline.
- Sort Tasks by Priority: Sort tasks by their priority.

## Getting Started

### Prerequisites
- Python 3.x
- `tasks.json` file in the project directory (initially an empty list: `[]`)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```
2. Create a `tasks.json` file in the project directory with an initial empty list:
```json
[]
```

## Usage
Run the main script to start the task manager:
```bash
python main.py
```
Follow the on-screen menu to perform various task management operations.

## Functions

### Task Operations

`add_task(tasks, task)`
Adds a new task to the list.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task` (dict): The task to be added.
- Returns: Updated list of tasks.

`remove_task(tasks, task_id)`
Removes a task by its ID.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be removed.
- Returns: Updated list of tasks.

`update_task(tasks, task_id, updated_task)`
Updates an existing task.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be updated.
    - `updated_task` (dict): The updated task details.
- Returns: Updated list of tasks.

`get_task(tasks, task_id)`
Retrieves a task by its ID.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be retrieved.
- Returns: The task details.

### Task Attribute Operations

`set_task_priority(tasks, task_id, priority)`
Sets the priority of a task.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be updated.
    - `priority` (str): The new priority level.
- Returns: Updated list of tasks.

`set_task_deadline(tasks, task_id, deadline)`
Sets the deadline for a task.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be updated.
    - `deadline` (str): The new deadline.
- Returns: Updated list of tasks.

`mark_task_as_completed(tasks, task_id)`
Marks a task as completed.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be marked as completed.
- Returns: Updated list of tasks.

`set_task_description(tasks, task_id, description)`
Sets the description for a task.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be updated.
    - `description` (str): The new description.
- Returns: Updated list of tasks.

### Task Filtering and Searching

`search_tasks_by_keyword(tasks, keyword)`
Searches tasks by a keyword in the description.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `keyword` (str): The keyword to search for.
- Returns: Tasks that contain the keyword in their description.

`filter_tasks_by_priority(tasks, priority)`
Filters tasks by priority.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `priority` (str): The priority level to filter by.
- Returns: Tasks with the specified priority.

`filter_tasks_by_status(tasks, status)`
Filters tasks by their completion status.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `status` (bool): The completion status to filter by.
- Returns: Tasks with the specified completion status.

`filter_tasks_by_deadline(tasks, deadline)`
Filters tasks by their deadline.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `deadline` (str): The deadline to filter by.
- Returns: Tasks with the specified deadline.

### Task Counting and Summarizing

`count_tasks(tasks)`
Returns the total number of tasks.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
- Returns: The total number of tasks.

`count_completed_tasks(tasks)`
Returns the number of completed tasks.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
- Returns: The number of completed tasks.

`count_pending_tasks(tasks)`
Returns the number of pending tasks.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
- Returns: The number of pending tasks.

`generate_task_summary(tasks)`
Generates a summary report of all tasks.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
- Returns: A summary report containing total, completed, and pending tasks.

### Task Sorting

`sort_tasks_by_deadline(tasks)`
Sorts tasks by their deadline.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
- Returns: The sorted list of tasks.

`sort_tasks_by_priority(tasks)`
Sorts tasks by their priority.
- Parameters:
    - `tasks` (list of dict): The current list of tasks.
- Returns: The sorted list of tasks.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
