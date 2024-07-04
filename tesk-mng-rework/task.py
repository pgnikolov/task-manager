class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def get_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        pass

    def get_tasks_inprogress(self):
        pass


class Task:
    priorities = ["low", "medium", "high"]

    def __init__(self, task_id, description, priority, deadline):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def set_task_priority(self, task_id, priority):
        pass

    def set_task_deadline(self, task_id, deadline):
        pass

    def mark_task_as_completed(self, task_id):
        pass

    def set_task_description(self, task_id, description):
        pass


class Manage:

    def update_task(self, task_id):
        pass

    def search_tasks_by_keyword(self, keyword):
        pass

    def filter_tasks_by_priority(self, priority):
        pass

    def filter_tasks_by_status(self, status):
        pass

    def filter_tasks_by_deadline(self, deadline):
        pass

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
