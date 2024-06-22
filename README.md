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

## Installation ⚙️
1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

## Usage ✍️
Run the main script to start the task manager:
```bash
python main.py
```
Follow the on-screen menu to perform various task management operations.

## Modules 📂

### **Task Module** 
The `task.py` module defines the `Task` class, which represents a task in the task manager. It includes validation methods and conversion methods for task attributes.

### **TaskManager Module**
The `task_manager.py` module defines the `TaskManager` class, which manages a list of tasks and provides methods to add, remove, update, filter, sort, and save/load tasks.

### **Main Script**
The `main.py` script provides a command-line interface for interacting with the `TaskManager`. It includes a menu for performing various task management operations.



## TaskManager 🔄

`add_task(task: Task) -> None` Adds a new task to the list.

<details>
  <summary>More...</summary>
 
    - Parameters:
       - `task (Task)`: The task to be added.
       
</details>

`remove_task(task_id: int) -> None`: Removes a task by its ID.

<details>
  <summary>More...</summary>
 
  - Parameters:
    - `task_id` (int): The ID of the task to be removed.
         
</details>


`update_task(task_id: int, updated_task: dict) -> None`: Updates an existing task.

<details>
  <summary>More...</summary>
 
  - Parameters:
    - `task_id` (int): The ID of the task to be updated.
    - `updated_task` (dict): The updated task details.
   
</details>


`get_task_by_id(task_id: int) -> Task`: Retrieves a task by its ID.

<details>
  <summary>More...</summary>
 
  - Parameters:
    - `task_id` (int): The ID of the task to be retrieved.
    
</details>


`save_tasks_to_file(file_path: str) -> None`: Saves the provided list of tasks to a specified file path.

<details>
  <summary>More...</summary>
 
  - Parameters:
      - `file_path` (str): The path to the file where tasks will be saved.
   
</details>

`load_tasks_from_file(file_path: str) -> None`: Loads the list of tasks from a specified file path.

<details>
  <summary>More...</summary>
   
    - Parameters:
       - `file_path (str)`: The path to the file from which tasks will be loaded.
       
</details>

## Task Attribute Operations 🧰

`set_task_priority(task_id: int, priority: str) -> None`: Sets the priority of a task.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `task_id` (int): The ID of the task to be updated.
     - `priority` (str): The new priority level.
   
</details>

`set_task_deadline(task_id: int, deadline: str) -> None`: Sets the deadline for a task.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `task_id` (int): The ID of the task to be updated.
     - `deadline` (str): The new deadline.
   
</details>

`mark_task_as_completed(task_id: int)-> None`: Marks a task as completed.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `task_id` (int): The ID of the task to be marked as completed.
    
</details>

`set_task_description(task_id: int, description: str) -> None`: Sets the description for a task.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `task_id` (int): The ID of the task to be updated.
     - `description` (str): The new description.
   

## Task Filtering and Searching 📑

`search_tasks_by_keyword(keyword: str) -> list`: Searches tasks by a keyword in the description.

<details>
  <summary>More...</summary>
 
  - Parameters:
      - `keyword` (str): The keyword to search for.
          
</details>

`filter_tasks_by_priority(priority: str) -> list`: Filters tasks by priority.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `priority` (str): The priority level to filter by.
   
</details>

`filter_tasks_by_status(status: str) -> list`: Filters tasks by their completion status.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `status` (str): The completion status to filter by.
   
</details>

`filter_tasks_by_deadline(deadline: str) -> list`: Filters tasks by their deadline.

<details>
  <summary>More...</summary>
 
  - Parameters:
     - `deadline` (str): The deadline to filter by.
       
</details>

## Task Counting and Summarizing 🧮

`count_tasks() ->`: Returns the total number of tasks.

`count_completed_tasks() -> int`: Returns the number of completed tasks.

`count_pending_tasks() -> int`: Returns the number of pending tasks.

`generate_task_summary() -> dict`: Generates a summary report of all tasks.

### Task Sorting 📑

`sort_tasks_by_deadline() -> None`: Sorts tasks by their deadline.

`sort_tasks_by_priority()-> None`: Sorts tasks by their priority.
    
</details>

### Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

### License ©️
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
