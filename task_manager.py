from datetime import datetime


def quicksort(arr, condition, ascending=True):
    """
    Sorts an array using the quicksort algorithm based on a given condition.
     Args:
        arr (list): The list of elements to sort.
        condition (function): A function that extracts the value to sort by.
        ascending (bool, optional): ascending order if True, else descending.
    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    middle = [x for x in arr if condition(x) == condition(pivot)]
    if ascending:
        left = [x for x in arr if (condition(x) < condition(pivot))]
        right = [x for x in arr if (condition(x) > condition(pivot))]
    else:
        left = [x for x in arr if (condition(x) > condition(pivot))]
        right = [x for x in arr if (condition(x) < condition(pivot))]
    return quicksort(left, condition, ascending) + middle + quicksort(right, condition, ascending)


def binary_search(arr, condition, target, ascending=True):
    """
    Binary search on a sorted array to find the target value based on a given condition.
    Args:
        arr (list): The sorted list of element.
        condition (function): A function that extracts the value to search by.
        target (any): The target value to find.
        ascending (bool, optional): array is sorted in ascending order if True, else descending.
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = condition(arr[mid])
        if mid_value == target:
            return mid
        if (ascending and mid_value < target) or (not ascending and mid_value > target):
            left = mid + 1
        else:
            right = mid - 1
    return -1


class TaskManager:
    """
    Manages a list of tasks with functions to add, remove, update, filter, and sort tasks.
    Attributes:
        PRIORITIES (list): A list of valid priorities for tasks.
        tasks (list): The list of tasks.
        tasks_by_deadline (list): The list of tasks sorted by deadline.
        tasks_by_priority (list): The list of tasks sorted by priority.
    """
    PRIORITIES = ["low", "medium", "high"]

    def __init__(self):
        self.tasks = []
        self.tasks_by_deadline = []
        self.tasks_by_priority = []

    def __validate_priority(self, priority):
        """
        Validates if the priority is in the allowed priorities.
        Args:
            priority (str): The priority level to validate.
        Raises:
            ValueError: If the priority is invalid.
        """
        if priority not in self.PRIORITIES:
            raise ValueError(f"Invalid priority. Must be one of {', '.join(self.PRIORITIES)}.")

    def __update_sorted_lists(self):
        self.tasks_by_deadline = quicksort(self.tasks, condition=lambda t: t[3] if t[3] else datetime.max)
        priority_order = {priority: i for i, priority in enumerate(self.PRIORITIES)}
        self.tasks_by_priority = quicksort(self.tasks, condition=lambda t: priority_order[t[2]])

    def add_task(self, task_id, description, priority, deadline_str, completed=False):
        """
        Adds a new task to the manager.
        Args:
            task_id (int): ID of the task.
            description (str): description of the task.
            priority (str):  priority of the task (low, medium, high).
            deadline_str (str): deadline for the task in DD-MM-YYYY format.
            completed (bool): Whether the task is completed. Defaults to False.
        Raises:
            ValueError: If the priority is invalid, the date format is incorrect or task ID already exists.
        """
        self.__validate_priority(priority)

        if any(task[0] == task_id for task in self.tasks):
            raise ValueError(f"Task with ID {task_id} already exists.")

        try:
            deadline = datetime.strptime(deadline_str, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")

        task = [task_id, description, priority, deadline, completed]
        self.tasks.append(task)
        self.__update_sorted_lists()

    def remove_task(self, task_id):
        """
        Removes a task.
        Args:
            task_id (int): ID of the task to remove.
        Returns:
            str: A message indicating if the task was found and removed.
        """
        for task in self.tasks:
            if task[0] == task_id:
                self.tasks.remove(task)
                self.__update_sorted_lists()
                return
        return "Task not found!"

    def update_task(self, task_id, updated_task):
        """
        Updates an existing task with new information.
        Args:
            task_id (int): ID of the task to update.
            updated_task (dict): A dictionary of the fields to update {"description": "New desc"}.
        Raises:
            ValueError: If any of the keys are invalid or the date format is incorrect.
        Returns:
            str: A message if task was found and updated.
        """
        valid_keys = {"description", "priority", "deadline", "completed"}
        for key in updated_task:
            if key not in valid_keys:
                raise ValueError(f"Invalid key: {key}. Valid keys are: {', '.join(valid_keys)}")

        for task in self.tasks:
            if task[0] == task_id:
                for key, value in updated_task.items():
                    if key == "description":
                        task[1] = value
                    elif key == "priority":
                        self.__validate_priority(value)
                        task[2] = value
                    elif key == "deadline":
                        try:
                            task[3] = datetime.strptime(value, "%d-%m-%Y")
                        except ValueError:
                            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")
                    elif key == "completed":
                        task[4] = value
                self.__update_sorted_lists()
                return
        return "Task not found!"

    def get_task(self, task_id):
        """
        Get task by its ID.
        Args:
            task_id (int): The ID of the task we need.
        Returns:
            list or str: The task details as a list, or a message if the task is not found.
        """
        task_index = next((i for i, task in enumerate(self.tasks) if task[0] == task_id), -1)
        if task_index != -1:
            return self.tasks[task_index]
        return f"Task with id {task_id} not found!"

    def filter_tasks_by_deadline(self, date_str, filter_type='before'):
        """
        Filters tasks based on their deadlines.
        Args:
            date_str (str): target date in DD-MM-YYYY format.
            filter_type (str): filter tasks 'before' or 'after' the target date. Default = 'before'.
        Raises:
            ValueError: If the date format is incorrect or the filter_type is invalid.
        Returns:
            list: A list of tasks that match the filter criteria.
        """
        # check for empty list
        if not self.tasks:
            return []
        try:
            target_date = datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")

        sorted_tasks = quicksort(self.tasks, condition=lambda t: t[3] if t[3] else datetime.max)

        if filter_type == 'before':
            bsindex = binary_search(sorted_tasks, condition=lambda t: t[3], target=target_date, ascending=True)
            if bsindex == -1:
                # If no exact match found, return all tasks before the target date
                filtered_tasks = [task for task in sorted_tasks if task[3] and task[3] < target_date]
            else:
                # Include all tasks before the target date
                filtered_tasks = [task for task in sorted_tasks[:bsindex + 1] if task[3] and task[3] < target_date]
        elif filter_type == 'after':
            bsindex = binary_search(sorted_tasks, condition=lambda t: t[3], target=target_date, ascending=False)
            if bsindex == -1:
                # If no exact match found, return all tasks after the target date
                filtered_tasks = [task for task in sorted_tasks if task[3] and task[3] > target_date]
            else:
                # Include all tasks after the target date
                filtered_tasks = [task for task in sorted_tasks[bsindex:] if task[3] and task[3] > target_date]
        else:
            raise ValueError("Invalid filter_type. Must be 'before' or 'after'.")
        return filtered_tasks

    def sort_tasks_by_deadline(self, ascending=True):
        """
        Sorts tasks by their deadlines.
        Args:
            ascending (bool, optional): Sort in ascending order if True, else descendin.
        Returns:
            str: A formatted string of the sorted tasks with deadlines.
        """
        # check for empty list
        if not self.tasks_by_deadline:
            return "No tasks to sort."

        sorted_tasks = self.tasks_by_deadline if ascending else list(reversed(self.tasks_by_deadline))
        result = "Sorted tasks with valid deadlines:\n"
        for task in sorted_tasks:
            result += f"Task ID: {task[0]}, Description: {task[1]}, Deadline: {task[3].strftime('%d-%m-%Y')}\n"
        return result.strip()

    def sort_tasks_by_priority(self, ascending=True):
        """
        Sorts the tasks by priority. The priority is sorted in order: "low", "medium", "high".
        If there are no tasks, the method returns an empty list.
        Args:
            ascending (bool, optional): True, sorts in ascending, False, sorts in descending.
        Returns:
            list of str: A list of strings, each string is a task
        """
        # check for empty list
        if not self.tasks_by_priority:
            return []

        sorted_tasks = self.tasks_by_priority if ascending else list(reversed(self.tasks_by_priority))
        result = []
        for task in sorted_tasks:
            result.append(f"Task ID: {task[0]}, Description: {task[1]}, Priority: {task[2]}")
        return result

    def find_task_by_deadline(self, date_str):
        """
        Finds and returns a list of tasks withdeadline wanted by user. Search goes in sorted list of tasks by deadline.
        Args:
            date_str (str): deadline date in the format "DD-MM-YYYY".
        Returns:
            list of list: A list of tasks, If no tasks returs empty list
        Raises:
            ValueError: If the provided date_str is not in the format "DD-MM-YYYY".
            -
        """
        try:
            target_date = datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")

        sorted_tasks = self.tasks_by_deadline
        bsindex = binary_search(sorted_tasks, condition=lambda t: t[3], target=target_date, ascending=True)
        matching_tasks = []
        if bsindex != -1:
            while bsindex < len(sorted_tasks) and sorted_tasks[bsindex][3] == target_date:
                matching_tasks.append(sorted_tasks[bsindex])
                bsindex += 1
        else:
            matching_tasks = []

        return matching_tasks

    def find_task_by_priority(self, priority):
        """
        Finds and returns a list of tasks with same priority, in already sorted list by priority
        Args:
            priority (str): The priority level to search "low", "medium", or "high".
        Returns:
            list of list: A list of tasks
        Raises:
            ValueError: If the provided priority is not valid.
        """
        self.__validate_priority(priority)
        sorted_tasks = self.tasks_by_priority
        priority_order = {p: i for i, p in enumerate(self.PRIORITIES)}
        target_priority_value = priority_order[priority]
        matching_tasks = [task for task in sorted_tasks if priority_order[task[2]] == target_priority_value]

        return matching_tasks


class TaskFileManager:
    """
    Handles saving and loading tasks from a file.
    Attributes:
        filename (str): name of the file to read from and write to.
    """

    def __init__(self, filename='tasks.txt'):
        self.filename = filename

    def save_tasks_to_file(self, tasks):
        with open(self.filename, "w") as f:
            for task in tasks:
                deadline_str = task[3].strftime('%d-%m-%Y') if task[3] else 'None'
                task_line = f"{task[0]},{task[1]},{task[2]},{deadline_str},{task[4]}\n"
                f.write(task_line)

    def load_tasks_from_file(self):
        tasks = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    task_data = line.strip().split(',')
                    task_id = int(task_data[0])
                    description = task_data[1]
                    priority = task_data[2] if task_data[2] else None
                    deadline = datetime.strptime(task_data[3], "%d-%m-%Y") if task_data[3] != 'None' else None
                    completed = task_data[4] == 'True'
                    tasks.append([task_id, description, priority, deadline, completed])
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. No tasks loaded.")
        return tasks


class TaskStatistics:
    """
    Provides static methods for generating task statistics.
    """
    @staticmethod
    def count_tasks(tasks):
        return len(tasks)

    @staticmethod
    def count_completed_tasks(tasks):
        return len([task for task in tasks if task[4]])

    @staticmethod
    def count_pending_tasks(tasks):
        return len([task for task in tasks if not task[4]])

    @staticmethod
    def generate_task_summary(tasks):
        total_tasks = TaskStatistics.count_tasks(tasks)
        completed_tasks = TaskStatistics.count_completed_tasks(tasks)
        pending_tasks = TaskStatistics.count_pending_tasks(tasks)
        return f"Total Tasks: {total_tasks}\nCompleted Tasks: {completed_tasks}\nPending Tasks: {pending_tasks}"
