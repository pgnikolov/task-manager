import json
from datetime import datetime
from task import Task


class TaskManager:
    """
        Manages a collection of tasks.
    Attributes:
        tasks (list): A list of Task instances.
    """
    def __init__(self):
        """Initializes a new TaskManager instance."""
        self.tasks = []

    def add_task(self, task: Task):
        """
            Adds a task to the task manager.
        Args:
            task (Task): The task to add.
        """
        self.tasks.append(task)

    def remove_task(self, task_id: int):
        """
            Removes a task from the task manager by its ID.
        Args:
            task_id (int): The ID of the task to remove.
        Raises:
            ValueError: If the task with the given ID is not found.
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    def update_task(self, task_id: int, updated_task: dict):
        """
            Updates a task in the task manager by its ID.
        Args:
            task_id (int): The ID of the task to update.
            updated_task (dict): A dictionary with the updated task attributes.
        Raises:
            ValueError: If the task with the given ID is not found.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.update(**updated_task)
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    def get_task_by_id(self, task_id: int):
        """
            Retrieves a task by its ID.
        Args:
            task_id (int): The ID of the task to retrieve.
        Returns:
            Task: The task with the given ID, or None if not found.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def set_task_priority(self, task_id: int, priority: str):
        """
            Sets the priority of a task.
        Args:
            task_id (int): The ID of the task to update.
            priority (str): The new priority for the task.
        Raises:
            ValueError: If the task with the given ID is not found.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = Task.validate_priority(priority)
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    def set_task_deadline(self, task_id: int, deadline: str):
        """
            Sets the deadline of a task.
        Args:
            task_id (int): The ID of the task to update.
            deadline (str): The new deadline for the task.
        Raises:
            ValueError: If the task with the given ID is not found.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.deadline = Task.validate_deadline(deadline)
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    def mark_task_as_completed(self, task_id: int):
        """
            Marks a task as completed.
        Args:
            task_id (int): The ID of the task to update.
        Raises:
            ValueError: If the task with the given ID is not found.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_as_completed()
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    def set_task_description(self, task_id: int, description: str):
        """
            Sets the description of a task.
        Args:
            task_id (int): The ID of the task to update.
            description (str): The new description for the task.
        Raises:
            ValueError: If the task with the given ID is not found.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.description = Task.validate_description(description)
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    def search_tasks_by_keyword(self, keyword: str):
        """
            Searches for tasks by keyword in their descriptions.
        Args:
            keyword (str): The keyword to search for.
        Returns:
            list: A list of tasks that contain the keyword in their descriptions.
        """
        return [task for task in self.tasks if keyword.lower() in task.description.lower()]

    def filter_tasks_by_priority(self, priority: str):
        """
            Filters tasks by priority.
        Args:
            priority (str): The priority to filter tasks by.
        Returns:
            list: A list of tasks with the given priority.
        """
        return [task for task in self.tasks if task.priority == priority]

    def filter_tasks_by_status(self, status: str):
        """
            Filters tasks by their completion status.
        Args:
            status (str): The status to filter tasks by ('completed' or 'pending').
        Returns:
            list: A list of tasks with the given status.
        """
        if status == "completed":
            return [task for task in self.tasks if task.completed]
        elif status == "pending":
            return [task for task in self.tasks if not task.completed]
        else:
            raise ValueError("Status must be 'completed' or 'pending'.")

    def filter_tasks_by_deadline(self, deadline: str):
        """
            Filters tasks by their deadline.
        Args:
            deadline (str): The deadline to filter tasks by.
        Returns:
            list: A list of tasks with deadlines before or on the given deadline.
        Raises:
            ValueError: If the deadline format is invalid.
        """
        validated_deadline = Task.validate_deadline(deadline)
        deadline_date = datetime.strptime(validated_deadline, '%d-%m-%Y').date()
        return [task for task in self.tasks if datetime.strptime(task.deadline, '%d-%m-%Y').date() <= deadline_date]

    def count_tasks(self):
        """
            Counts the total number of tasks.
        Returns:
            int: The total number of tasks.
        """
        return len(self.tasks)

    def count_completed_tasks(self):
        """
            Counts the number of completed tasks.
        Returns:
            int: The number of completed tasks.
        """
        return len([task for task in self.tasks if task.completed])

    def count_pending_tasks(self):
        """
            Counts the number of pending tasks.
        Returns:
            int: The number of pending tasks.
        """
        return len([task for task in self.tasks if not task.completed])

    def generate_task_summary(self):
        """
            Generates a summary of tasks, including total, completed, and pending tasks
        Returns:
            dict: A dictionary containing the summary of tasks.
        """
        return {
            "total": self.count_tasks(),
            "completed": self.count_completed_tasks(),
            "pending": self.count_pending_tasks()
        }

    def save_tasks_to_file(self, file_path: str):
        """
            Saves tasks to a file in JSON format.
        Args:
            file_path (str): The path to the file where tasks will be saved.
        """
        with open(file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def load_tasks_from_file(self, file_path: str):
        """
            Loads tasks from a file in JSON format.
        Args:
            file_path (str): The path to the file from which tasks will be loaded.
        """
        with open(file_path, 'r') as file:
            tasks_data = json.load(file)
            self.tasks = [Task(**task_data) for task_data in tasks_data]

    def sort_tasks_by_deadline(self):
        """Sorts tasks by their deadlines in ascending order."""
        self.tasks.sort(key=lambda task: datetime.strptime(task.deadline, '%d-%m-%Y'))

    def sort_tasks_by_priority(self):
        """Sorts tasks by their priorities in the order 'low', 'medium', 'high'."""
        priority_order = {priority: index for index, priority in enumerate(Task.VALID_PRIORITIES)}
        self.tasks.sort(key=lambda task: priority_order[task.priority])
