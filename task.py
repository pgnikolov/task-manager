from datetime import datetime


class Task:
    """
        Single task with an ID, description, priority, deadline, and completion status.
    Attributes:
        id (int): Task ID.
        description (str): Task description.
        priority (int): Task priority - low, medium or high
        deadline (datetime): Task deadline in format DD-MM-YYYY
        completed (bool): Task completion status.
    """
    VALID_PRIORITIES = ["low", "medium", "high"]

    def __init__(self, task_id: int, description: str, priority: str, deadline: str):
        """
            Initializes a new Task instance.
        Args:
            task_id (int): The unique identifier for the task.
            description (str): The description of the task.
            priority (str): The priority of the task.
            deadline (str): The deadline for the task.
        Raises:
            ValueError: If the task ID is not an integer.
            ValueError: If the description is empty.
            ValueError: If the priority is not one of the valid priorities.
            ValueError: If the deadline format is invalid or is set to a past date.
        """
        self.id = self.validate_id(task_id)
        self.description = self.validate_description(description)
        self.priority = self.validate_priority(priority)
        self.deadline = self.validate_deadline(deadline)
        self.completed = False

    def update(self, description: str = None, priority: str = None, deadline: str = None):
        """
            Updates the task's attributes.
        Args:
            description (str, optional): The new description for the task.
            priority (str, optional): The new priority for the task.
            deadline (str, optional): The new deadline for the task.
        """
        if description:
            self.description = self.validate_description(description)
        if priority:
            self.priority = self.validate_priority(priority)
        if deadline:
            self.deadline = self.validate_deadline(deadline)

    def mark_as_completed(self):
        """Marks the task as completed."""
        if not self.completed:
            self.completed = True

    # STATIC METHOD FOR THE CLASS
    @staticmethod
    def validate_id(task_id):
        """
            Validates the task ID.
        Args:
            task_id (int): The task ID to validate.
        Returns:
            int: The validated task ID.
        Raises:
            ValueError: If the task ID is not an integer.
        """
        if not isinstance(task_id, int):
            raise ValueError("Task ID must be an integer.")
        return task_id

    @staticmethod
    def validate_description(description):
        """
            Validates the task description.
        Args:
            description (str): The task description to validate.
        Returns:
            str: The validated task description.
        Raises:
            ValueError: If the description is empty.
        """
        if not description:
            raise ValueError("Description cannot be empty.")
        return description.capitalize()

    @staticmethod
    def validate_priority(priority):
        """
             Validates the task priority.
        Args:
            priority (str): The task priority to validate.
        Returns:
            str: The validated task priority.
        Raises:
            ValueError: If the priority is not one of the valid priorities.
        """
        if priority not in Task.VALID_PRIORITIES:
            raise ValueError(f"Priority must be one of {Task.VALID_PRIORITIES}.")
        return priority

    @staticmethod
    def validate_deadline(deadline):
        """
            Validates the task deadline.
        Args:
            deadline (str): The task deadline to validate.
        Returns:
            str: The validated task deadline.
        Raises:
            ValueError: If the deadline format is invalid or is set to a past date.
        """
        try:
            date = datetime.strptime(deadline, '%d-%m-%Y')
            if date.date() < datetime.today().date():
                raise ValueError("Deadline cannot be earlier than today's date.")
        except ValueError:
            raise ValueError("Invalid date format. Please enter date in format DD-MM-YYYY.")
        return deadline

    def task_to_dict(self):
        """
            Converts the task to a dictionary representation.
        Returns:
            dict: The dictionary representation of the task.
        """
        return {
            "id": self.id,
            "description": self.description,
            "priority": self.priority,
            "deadline": self.deadline,
            "completed": self.completed
        }

    def __repr__(self):
        """
            Returns a string representation of the task.
        Returns:
            str: The string representation of the task.
        """
        return (f"Task(id={self.id}, description='{self.description}', priority='{self.priority}', "
                f"deadline='{self.deadline}', completed={self.completed})")
