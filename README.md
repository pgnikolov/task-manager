# Task Manager Application 📑	
![readmemd](https://github.com/pgnikolov/task-manager/assets/151896883/5e60450b-4b26-44ca-9f04-c6a6ea5ce108)

## Introduction 🎦


This application is designed to help you organize and manage tasks effectively.  With advanced features for sorting, searching, 
and filtering, this application ensures that you can easily prioritize and track your tasks. Whether for personal use or team projects,
this application helps manage deadlines, priorities, and completion statuses effectively.

## Leveraging Quicksort and Binary Search 🧠
Quicksort and Binary Search enhance the performance and efficiency of task management operations:

- **Quicksort** is utilized to sort tasks based on deadlines and priorities. While Quicksort traditionally sorts arrays of numbers, we've adapted it to work with complex task objects. Instead of simply comparing numerical values, the algorithm extracts and compares specific attributes (like deadlines or priority levels) from each task. This customized approach allows for efficient sorting tailored to the application's needs.

- **Binary Search** is implemented for quickly finding tasks based on their deadlines. In a standard Binary Search, the algorithm searches for a specific value in a sorted array. Here, we've modified it to search within an array of tasks, where the search is based on a particular attribute, such as the task's deadline. This adaptation provides a fast and effective way to locate tasks within large datasets.

## Algorithmic Changes ⚙️

- **Quicksort Modifications:** Condition-based Sorting: Instead of direct comparisons, the algorithm uses a condition function to extract the relevant attribute (deadline or priority) from each task for comparison.
- **Binary Search Adjustments:** The search focuses on task attributes (like deadlines), requiring the condition function to extract these attributes for comparison during the search process. The search is flexible, supporting both ascending and descending sorted arrays, which is crucial for tasks sorted by either earliest or latest deadlines.




## Table of Contents 📝

- Requirements 
- Recommended Modules 
- Installation 
- Configuration 
- Usage 
- Troubleshooting & FAQ 
- Maintainers 
- Contributing
- License

## Requirements 🎗️

To run the Task Manager application, ensure your environment meets the following requirements:
- Python: Version 3.x 
- datetime module: Typically included in Python's standard library

## Recommended Modules 👌
This application does not require any additional Python modules beyond the standard library.

## Installation ⚙️
1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```
2. Create a virtual environment (optional but recommended) 💻
```bash
python3 -m venv venv
source venv/bin/activate 
```
3. Install dependencies: 
If your Python environment does not have datetime module installed (highly unlikely), you can install it using pip:
```bash
pip install datetime
```

## Configuration  🛠️

Before running the application, ensure you configure the following aspects:
- Priority Levels: The application supports task priorities such as low, medium, and high. 
- Deadline Format: Dates should be formatted as DD-MM-YYYY.

## Usage ✍️

### Adding a Task
Add a new task with specific details including description, priority, and an optional deadline.
```python
from task_manager import TaskManager

task_manager = TaskManager()
task_manager.add_task(task_id=1, description="Complete project proposal", priority="high", deadline_str="15-07-2024")
```
### Removing a Task 🗑️
Remove a task using its ID.
```python
task_manager.remove_task(1)
```

### Updating a Task 🆕
Update an existing task’s details like description, priority, deadline, or completion status.
```python
task_manager.update_task(2, {"description": "Finalize project proposal and submit", "completed": True})
```

### Searching for Tasks 🔍
Search for tasks by their deadline or priority.
```python
tasks_with_deadline = task_manager.find_task_by_deadline("20-08-2024")
tasks_with_priority = task_manager.find_task_by_priority("medium")
```

### Filtering Tasks 🗃️
Filter tasks by deadlines either before or after a specified date.
```python
tasks_before_date = task_manager.filter_tasks_by_deadline("21-08-2024", filter_type='before')
tasks_after_date = task_manager.filter_tasks_by_deadline("21-08-2024", filter_type='after')
```

### Sorting Tasks 🗂️
Sort tasks by their deadlines or priorities in ascending or descending order.
```python
sorted_by_deadline = task_manager.sort_tasks_by_deadline(ascending=True)
sorted_by_priority = task_manager.sort_tasks_by_priority(ascending=True)
```

### Saving and Loading Tasks 💾
Tasks can be saved to a file and loaded back into the application.
```python
from task_manager import TaskFileManager

file_manager = TaskFileManager('tasks.txt')
file_manager.save_tasks_to_file(task_manager.tasks)
loaded_tasks = file_manager.load_tasks_from_file()
```

### Generating Task Statistics 📊
Generate summaries and statistics for your tasks.
```python
from task_manager import TaskStatistics

summary = TaskStatistics.generate_task_summary(task_manager.tasks)
print(summary)
```

## Troubleshooting & FAQ ❔
 - **Task not found?** Ensure the task ID exists before attempting to update or remove it. 
 - **Invalid date** format? Ensure all dates follow the DD-MM-YYYY format. 
 - **Priority level issues?** Use only "low", "medium", or "high" as valid priority levels.

### Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

### License ©️
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
