# Task Manager 📑	

 <img src="https://github.com/pgnikolov/task-manager/assets/151896883/9324d27a-9ef9-4a0c-9e02-f74876ce36f9" width="750" height="400">
 
A simple command-line task manager application written in Python. This project allows users to manage tasks by adding, updating, removing, and filtering tasks based on various criteria.

## Features 🧰

* :heavy_plus_sign: Add Task: Add new tasks to the list.
* :x: Remove Task: Remove tasks by their ID.
* :arrows_counterclockwise: Update Task: Update task details such as description, priority, and deadline.
* :mag: Get Task: Retrieve task details by their ID.
* :chart_with_upwards_trend: Set Task Priority: Set the priority of a task.
* :alarm_clock: Set Task Deadline: Set the deadline for a task.
* :white_check_mark: Mark Task as Completed: Mark tasks as completed.
* :memo: Set Task Description: Set or update the description of a task.
* :mag_right: Search Tasks by Keyword: Search tasks by a keyword in their description.
* :pushpin: Filter Tasks by Priority: Filter tasks by their priority.
* :vertical_traffic_light: Filter Tasks by Status: Filter tasks by their completion status (completed or pending).
* :calendar: Filter Tasks by Deadline: Filter tasks by their deadline.
* :1234: Count Tasks: Get the total number of tasks.
* :ballot_box_with_check: Count Completed Tasks: Get the number of completed tasks.
* :hourglass_flowing_sand: Count Pending Tasks: Get the number of pending tasks.
* :bar_chart: Generate Task Summary: Generate a summary report of all tasks.
* :floppy_disk: Save Tasks: Saves tasks to json file.
* :inbox_tray: Load Tasks: Loads saved tasks from file.
* :arrow_heading_down: Sort Tasks by Deadline: Sort tasks by their deadline.
* :arrow_heading_up: Sort Tasks by Priority: Sort tasks by their priority.
* :id: ID Validation: Ensure the id number is integer.
* :1234: Priority Validation: Checks if the priority entered by user is one of "low","medium" or "high".
* :alarm_clock: Deadline Validation: Checks the date format and if the date is not past.
* :memo: Description Validation: Checks if the description is not empty string.

## Getting Started 💻

### Prerequisites
- Python 3.x

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

## Usage
Run the main script to start the task manager:
```bash
python main.py
```
Follow the on-screen menu to perform various task management operations.


## Task Operations 🔄

`add_task(tasks, task)`: Adds a new task to the list.

<details>
  <summary>More...</summary>
 
  - Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task` (dict): The task to be added.
  - Returns: Updated list of tasks.
   
</details>


`remove_task(tasks, task_id)`: Removes a task by its ID.

<details>
  <summary>More...</summary>
 
  - Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be removed.
  - Returns: Updated list of tasks.
   
</details>


`update_task(tasks, task_id, updated_task)`: Updates an existing task.

<details>
  <summary>More...</summary>
 
  - Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be updated.
    - `updated_task` (dict): The updated task details.
  - Returns: Updated list of tasks.
   
</details>


`get_task(tasks, task_id)`: Retrieves a task by its ID.

<details>
  <summary>More...</summary>
 
  - Parameters:
    - `tasks` (list of dict): The current list of tasks.
    - `task_id` (int): The ID of the task to be retrieved.
  - Returns: The task details.
   
</details>


`save_tasks_to_file(tasks, file_path)`: Saves the provided list of tasks to a specified file path.

<details>
  <summary>More...</summary>
 
  - Parameters:
      - tasks (list of dict): The current list of tasks.
      - file_path (str): The path to the file where tasks will be saved.
  - Returns:
      - None
   
</details>

## Task Attribute Operations 🧰

`set_task_priority(tasks, task_id, priority)`: Sets the priority of a task.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
     - `task_id` (int): The ID of the task to be updated.
     - `priority` (str): The new priority level.
  - Returns: Updated list of tasks.
   
</details>

`set_task_deadline(tasks, task_id, deadline)`: Sets the deadline for a task.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
     - `task_id` (int): The ID of the task to be updated.
     - `deadline` (str): The new deadline.
  - Returns: Updated list of tasks.
   
</details>

`mark_task_as_completed(tasks, task_id)`: Marks a task as completed.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
     - `task_id` (int): The ID of the task to be marked as completed.
  - Returns: Updated list of tasks.
   
</details>

`set_task_description(tasks, task_id, description)`: Sets the description for a task.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
     - `task_id` (int): The ID of the task to be updated.
     - `description` (str): The new description.
  - Returns: Updated list of tasks.
   
</details>

`load_tasks_from_file(file_path)`: Loads the list of tasks from a specified file path.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
     - `task_id` (int): The ID of the task to be updated.
     - `description` (str): The new description.
  - Returns: Updated list of tasks.
   
</details>

## Task Filtering and Searching 📑

`search_tasks_by_keyword(tasks, keyword)`: Searches tasks by a keyword in the description.

<details>
  <summary>More...</summary>
 
  - Parameters:
      - `tasks` (list of dict): The current list of tasks.
      - `keyword` (str): The keyword to search for.
  - Returns: Tasks that contain the keyword in their description.
   
</details>

`filter_tasks_by_priority(tasks, priority)`: Filters tasks by priority.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
     - `priority` (str): The priority level to filter by.
  - Returns: Tasks with the specified priority.
   
</details>

`filter_tasks_by_status(tasks, status)`: Filters tasks by their completion status.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
     - `status` (bool): The completion status to filter by.
  - Returns: Tasks with the specified completion status.
   
</details>

`filter_tasks_by_deadline(tasks, deadline)`: Filters tasks by their deadline.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
     - `deadline` (str): The deadline to filter by.
  - Returns: Tasks with the specified deadline.
   
</details>

## Task Counting and Summarizing 🧮

`count_tasks(tasks)`: Returns the total number of tasks.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
  - Returns: The total number of tasks.
   
</details>

`count_completed_tasks(tasks)`: Returns the number of completed tasks.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
  - Returns: The number of completed tasks.
   
</details>

`count_pending_tasks(tasks)`: Returns the number of pending tasks.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
  - Returns: The number of pending tasks.

</details>

`generate_task_summary(tasks)`: Generates a summary report of all tasks.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
  - Returns: A summary report containing total, completed, and pending tasks.

</details>

### Task Sorting 📑

`sort_tasks_by_deadline(tasks)`: Sorts tasks by their deadline.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
  - Returns: The sorted list of tasks.
</details>

`sort_tasks_by_priority(tasks)`: Sorts tasks by their priority.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `tasks` (list of dict): The current list of tasks.
  - Returns: The sorted list of tasks.
    
</details>

### Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

### License ©️
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
