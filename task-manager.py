import json
from datetime import datetime


class Task:
    """
        Single task with an ID, description, priority, deadline, and completion status.
    Attributes:
        task_id (int): Task ID.
        description (str): Task description.
        priority (int): Task priority - low, medium or high
        deadline (datetime): Task deadline in format DD-MM-YYYY
        completed (bool): Task completion status.
        PRIORITIES (list): Possible options for task priority.
    """
    PRIORITIES = ["low", "medium", "high"]

    def __init__(self, task_id, description=None, priority=None, deadline=None, completed=False):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = completed

    def set_task_priority(self, priority):
        if priority in self.PRIORITIES:
            self.priority = priority
        else:
            return f"Invalid priority. Must be one of {', '.join(self.PRIORITIES)}."

    def set_deadline(self, deadline):
        if deadline:
            try:
                deadline_date = datetime.strptime(deadline, "%d-%m-%Y")
                if deadline_date > datetime.now():
                    self.deadline = deadline_date
                else:
                    raise ValueError("Deadline cannot be in the past.")
            except ValueError:
                raise ValueError("Invalid deadline format. Use DD-MM-YYYY.")
        else:
            self.deadline = None

    def task_to_dict(self):
        return {
            "description": self.description,
            "priority": self.priority,
            "deadline": self.deadline.strftime("%d-%m-%Y") if self.deadline else None,
            "completed": self.completed
        }


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        """
            Adds a task to the task manager.
        Args:
            task (Task): The task to add.
        """
        self.tasks[task.task_id] = task

    def remove_task(self, task_id):
        """
            Removes a task from the task manager by its ID.
        Args:
            task_id : The ID of the task to remove.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            return "Task not found!"

    def update_task(self, task_id, updated_task):
        """
            Updates a task in the task manager by its ID.
        Args:
            task_id: The ID of the task to update.
            updated_task (dict): A dictionary with the updated task attributes.
        """
        if task_id in self.tasks:
            self.tasks[task_id] = updated_task
        else:
            return "Task not found!"

    def get_task(self, task_id):
        """
            Retrieves a task by its ID.
        Args:
            task_id: The ID of the task to retrieve.
        Returns:
            Task: The task with the given ID, or None if not found.
        """
        if task_id in self.tasks:
            return self.tasks.get(task_id)
        else:
            return f"Task with id {task_id} not found!"

    def set_task_priority(self, task_id, priority):
        """
            Sets the priority of a task.
        Args:
            task_id: The ID of the task to update.
            priority (str): The new priority for the task.
        Returns:
            str: A message if task with task_id doesn't exist.
        """
        if task_id in self.tasks:
            self.tasks[task_id].priority = priority
        else:
            return f"Task with id {task_id} not found!"

    def set_task_deadline(self, task_id, deadline):
        """
            Sets the deadline of a task.
        Args:
            task_id: The ID of the task to update.
            deadline (str): The new deadline for the task.
        Returns:
            str: A message if task with task_id doesn't exist.
        """
        if task_id in self.tasks:
            self.tasks[task_id].deadline = deadline
        else:
            return f"Task with id {task_id} not found!"

    def mark_task_as_completed(self, task_id):
        """
            Marks a task as completed.
        Args:
            task_id: The ID of the task to update.
        Returns:
            str: A message if task with task_id doesn't exist.
        """
        if task_id in self.tasks:
            self.tasks[task_id].completed = True
        else:
            return f"Task with id {task_id} not found!"

    def set_task_description(self, task_id, description):
        """
            Sets the description of a task.
        Args:
            task_id: The ID of the task to update.
            description (str): The new description for the task.
        Returns:
            str: A message if task with task_id doesn't exist.
        """
        if task_id in self.tasks:
            self.tasks[task_id].description = description
        else:
            return f"Task with id {task_id} not found!"

    def search_tasks_by_keyword(self, keyword):
        """
            Searches for tasks by keyword in their descriptions.
        Args:
            keyword (str): The keyword to search for.
        Returns:
            list: A list of tasks that contain the keyword in their descriptions.
            str: A message if tasks with keyword in their descriptions are found.
        """
        task_keyword = [task for task in self.tasks.values() if keyword.lower() in task.description.lower()]
        if not task_keyword:
            return f"No tasks found with keyword in their description '{keyword}'!"
        else:
            return task_keyword

    def filter_tasks_by_priority(self, priority):
        """
            Filters tasks by priority.
        Args:
            priority (str): The priority to filter tasks by.
        Returns:
            list: A list of tasks with the given priority.
            str: A message if the given priority is not valid.
        """
        if priority in Task.PRIORITIES:
            return [task for task in self.tasks.values() if task.priority == priority]
        else:
            return f"{priority} is not a valid priority."

    def filter_completed(self, status):
        """
            Filters tasks by their completion status.
        Args:
            status (str): The status to filter tasks by ('completed' or 'pending').
        Returns:
            list: A list of tasks with the given status.
            str: A message if the given status is not valid.
        """
        if status == 'completed':
            completed_tasks = [task for task in self.tasks.values() if task.completed]
        elif status == 'pending':
            completed_tasks = [task for task in self.tasks.values() if not task.completed]
        else:
            return f"{status} is not a valid status."
        return completed_tasks

    def filter_tasks_by_deadline(self, deadline):
        """
            Filters tasks by their deadline.
        Args:
            deadline (str): The deadline to filter tasks by.
        Returns:
            list: A list of tasks with deadlines before or on the given deadline.
        """
        return [task for task in self.tasks.values() if task.deadline == deadline]

    def count_tasks(self):
        """
            Counts the total number of tasks.
        Returns:
            int: The total number of tasks.
            str: A message if there is no tasks found.
        """
        if self.tasks:
            return len(self.tasks)
        else:
            return "No tasks found."

    def count_completed_tasks(self):
        """
            Counts the number of completed tasks.
        Returns:
            int: The number of completed tasks.
            str: A message if completed tasks are not found.
        """
        completed_tasks = self.filter_completed('completed')
        if not completed_tasks:
            return "No completed tasks found."
        else:
            return len(completed_tasks)

    def count_pending_tasks(self):
        """
            Counts the number of pending tasks.
        Returns:
            int: The number of pending tasks.
            str: A message if pending tasks are not found.
        """
        pending_tasks = self.filter_tasks_by_priority('pending')
        if not pending_tasks:
            return "No pending tasks found."
        else:
            return len(pending_tasks)

    def generate_task_summary(self):
        """
            Generates a summary of tasks, including total, completed, and pending tasks
        """
        total_tasks = self.count_tasks()
        completed_tasks = self.count_completed_tasks()
        pending_tasks = self.count_pending_tasks()
        return f"Total Tasks: {total_tasks}\nCompleted Tasks: {completed_tasks}\nPending Tasks: {pending_tasks}"

    def save_tasks_to_file(self):
        """
            Saves tasks to a file in JSON format.
        """
        task_data = [task.to_dict() for task in self.tasks.values()]
        with open('tasks.json', "w") as f:
            json.dump(task_data, f, indent=4)

    def load_tasks_from_file(self):
        """
            Loads tasks from i JSON file.
        """
        try:
            with open('tasks.json', "r") as f:
                task_data = json.load(f)
            for task_dict in task_data:
                task = Task(
                    task_dict["description"],
                    task_dict["priority"],
                    datetime.strptime(task_dict["deadline"], "%d-%m-%Y") if task_dict["deadline"] else None,
                    task_dict["completed"])
                self.tasks[task.task_id] = task
        except FileNotFoundError:
            pass

    def sort_tasks_by_deadline(self, ascending=True):
        """
            Sorts tasks by their deadlines in ascending order.
        Args:
            ascending (bool): Sort tasks by their deadlines in ascending order or not.
        Returns:
            str: A msg if there are task with not valid or missing deadlines.
            str: A message with all tasks sorted by their deadlines.
        """
        tasks = list(self.tasks.values())
        tasks_with_deadlines = []
        for task in tasks:
            if hasattr(task, 'deadline') and task.deadline is not None:
                tasks_with_deadlines.append(task)
            else:
                print(f"Task {task.id} does not have a valid deadline.")
        tasks_with_deadlines.sort(key=lambda task: task.deadline, reverse=not ascending)
        print("Sorted tasks with valid deadlines:")
        for task in tasks_with_deadlines:
            print(f"Task ID: {task.id}, Description: {task.description}, Deadline: {task.deadline}")

    def sort_tasks_by_priority(self, ascending=True):
        """
        Sorts tasks by their priorities in ascending order.

        Args:
            ascending (bool): Sort tasks by their priorities in ascending order or not.

        Returns:
            str: A message with all tasks sorted by their priorities.
        """
        priority_order = {'low': 1, 'medium': 2, 'high': 3}
        sorted_tasks = sorted(self.tasks, key=lambda x: priority_order[x['priority']], reverse=not ascending)
        result = "Tasks sorted by priority:\n"
        for task in sorted_tasks:
            result += f"Task: {task['name']}, Priority: {task['priority']}\n"
        return result.strip()
