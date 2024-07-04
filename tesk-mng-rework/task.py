from datetime import datetime


def deadline_to_date(func):
    def wrapper(*args, **kwargs):
        deadline_str = args[1]  # Assuming deadline is the second argument after self

        try:
            deadline_date = datetime.strptime(deadline_str, '%d-%m-%Y').date()
            return func(*args, **kwargs)
        except ValueError:
            raise ValueError("Invalid date format. Please enter date in format DD-MM-YYYY.")

    return wrapper

class Task:
    priorities = ["low", "medium", "high"]

    def __init__(self, task_id, description, priority, deadline):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def set_task_priority(self, priority):
        if priority in self.priorities:
            self.priority = priority
        else:
            return f"{priority} is not a valid priority"

    @deadline_to_date
    def set_task_deadline(self, deadline):
        if deadline > datetime.today():
            self.deadline = deadline
            return f"Deadline set to {self.deadline}"
        else:
            return f"Deadline must be in the future"

    def mark_task_as_completed(self):
        if not self.completed:
            self.completed = True
        else:
            return f"Task {self.task_id} is already completed"

    def set_task_description(self, description):
        self.description = description


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        completed_tasks = []
        for task in self.tasks:
            if task.completed:
                completed_tasks.append(task)
        return completed_tasks

    def get_tasks_inprogress(self):
        tasks_inprogress = []
        for task in self.tasks:
            if not task.completed:
                tasks_inprogress.append(task)
        return tasks_inprogress


class Manage:

    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager

    def update_task(self, task_id):
        pass

    def search_tasks_by_keyword(self, keyword):
        pass

    def filter_tasks_by_priority(self, priority):
        pass

    def filter_tasks_by_status(self, status):
        pass

    def filter_tasks_by_deadline(self, deadline):
        return [task for task in TaskManager().tasks if datetime.strptime(task.deadline, '%d-%m-%Y').date() <= deadline]

    def generate_task_summary(self):
        pass

    def save_tasks_to_file(self, file_path):
        pass

    def load_tasks_from_file(self, file_path):
        pass

    def sort_tasks_by_deadline(self):
        pass

    def sort_tasks_by_priority(self):
        pass


task1 = Task('T001', 'Example1 Task', 'low', '12-12-2024')
task2 = Task('T002', 'Example2 Task', 'low', '13-12-2024')
task3 = Task('T003', 'Example3 Task', 'low', '14-12-2024')
# task_manager = TaskManager()
# task_manager.add_task(task1)
# task_manager.add_task(task2)
# task_manager.add_task(task3)
print(task1.set_task_deadline("01-12-2025"))  # Valid date
print(task2.set_task_deadline("31-12-2020"))  # Date in the past