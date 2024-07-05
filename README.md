# Task Manager Application 📑	

 <img src="https://github.com/pgnikolov/task-manager/assets/151896883/9324d27a-9ef9-4a0c-9e02-f74876ce36f9" width="750" height="400">
 
## Introduction

This application is designed to help you organize and manage tasks effectively. Whether you're managing personal tasks, team projects, or daily activities, this tool provides a simple way to track tasks, set priorities, manage deadlines, and monitor completion status.

## Table of Contents

- Requirements 
- Recommended Modules 
- Installation 
- Configuration 
- Usage 
- Troubleshooting & FAQ 
- Maintainers 
- Contributing
- License

## Requirements

To run the Task Manager application, ensure your environment meets the following requirements:
- Python: Version 3.x 
- datetime module: Typically included in Python's standard library

## Recommended Modules
This application does not require any additional Python modules beyond the standard library.

## Installation ⚙️
1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```
2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate 
```
3. Install dependencies:
If your Python environment does not have datetime module installed (highly unlikely), you can install it using pip:
```bash
pip install datetime
```

## Configuration

Before running the application, ensure you configure the following aspects:
- Priority Levels: The application supports task priorities such as low, medium, and high. 
- Deadline Format: Dates should be formatted as DD-MM-YYYY.

## Usage ✍️

### Adding a Task
To add a new task, use the `add_task()` method with the appropriate details including description, priority, and optional deadline.
```python
from task_manager import Task, TaskManager

# Example usage
task_manager = TaskManager()

task1 = Task(task_id=1, description="Complete project proposal", priority="high", deadline="15-07-2024")
task_manager.add_task(task1)
```
### Updating a Task
You can update a task's details such as description, priority, deadline, or completion status using the `update_task()` method.
```python
# Example usage
updated_task_data = {
    "description": "Finalize project proposal and submit",
    "deadline": "20-07-2024"
}
task_manager.update_task(1, updated_task_data)
```

### Marking a Task as Completed
Use the `mark_task_as_completed()` method to mark a task as completed.
```python
# Example usage
task_manager.mark_task_as_completed('T01')
```

### Filtering Tasks
You can filter tasks by priority or completion status using methods like `filter_tasks_by_priority()` and `filter_completed()`.
```python
# Example usage
high_priority_tasks = task_manager.filter_tasks_by_priority('high')
completed_tasks = task_manager.filter_completed('completed')
```

### Saving and Loading Tasks
Tasks can be saved to a JSON file using `save_tasks_to_file()` and loaded back into the Task Manager using `load_tasks_from_file()`.
```python
# Example usage
task_manager.save_tasks_to_file()
task_manager.load_tasks_from_file('tasks.json')
```

## Troubleshooting & FAQ
Task not found when performing operations?
If you encounter "Task not found" errors while updating, removing, or retrieving tasks, ensure that the task ID exists in the system. Double-check the task ID and try again.

Invalid deadline format?
When setting deadlines, use the format `DD-MM-YYYY`. Dates should be valid and in the future.

How to mark a task as completed?
To mark a task as completed, use the `mark_task_as_completed(task_id)` method. Ensure the task ID exists and is valid.

### Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

### License ©️
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
