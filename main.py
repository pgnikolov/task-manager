from task_manager import TaskManager
from task import Task


def main():
    """
    The main function to interact with the TaskManager through a command-line interface.
    """
    task_manager = TaskManager()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Update task")
        print("4. View task")
        print("5. Set task priority")
        print("6. Set task deadline")
        print("7. Mark task as completed")
        print("8. Set task description")
        print("9. Search tasks by keyword")
        print("10. Filter tasks by priority")
        print("11. Filter tasks by status")
        print("12. Filter tasks by deadline")
        print("13. Count total tasks")
        print("14. Count completed tasks")
        print("15. Count pending tasks")
        print("16. Generate task summary")
        print("17. Save tasks to file")
        print("18. Load tasks from file")
        print("19. Sort tasks by deadline")
        print("20. Sort tasks by priority")
        print("21. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                task_id = int(input("Enter task ID: "))
                description = input("Enter task description: ")
                priority = input("Enter task priority (low, medium, high): ").lower()
                deadline = input("Enter task deadline (DD-MM-YYYY): ")
                task = Task(task_id, description, priority, deadline)
                task_manager.add_task(task)
                print("Task added successfully.")
            except ValueError as e:
                print(e)
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to remove: "))
                task_manager.remove_task(task_id)
                print("Task removed successfully.")
            except ValueError as e:
                print(e)
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                description = input("Enter new description (leave blank to keep current): ")
                priority = input("Enter new priority (leave blank to keep current): ").lower()
                deadline = input("Enter new deadline (leave blank to keep current): ")
                updated_task = {
                    "description": description if description else None,
                    "priority": priority if priority else None,
                    "deadline": deadline if deadline else None
                }
                task_manager.update_task(task_id, updated_task)
                print("Task updated successfully.")
            except ValueError as e:
                print(e)
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to view: "))
                task = task_manager.get_task_by_id(task_id)
                if task:
                    print(task)
                else:
                    print("Task not found.")
            except ValueError as e:
                print(e)
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to set priority: "))
                priority = input("Enter new priority (low, medium, high): ").lower()
                task_manager.set_task_priority(task_id, priority)
                print("Task priority set successfully.")
            except ValueError as e:
                print(e)
        elif choice == '6':
            try:
                task_id = int(input("Enter task ID to set deadline: "))
                deadline = input("Enter new deadline (DD-MM-YYYY): ")
                task_manager.set_task_deadline(task_id, deadline)
                print("Task deadline set successfully.")
            except ValueError as e:
                print(e)
        elif choice == '7':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                task_manager.mark_task_as_completed(task_id)
                print("Task marked as completed.")
            except ValueError as e:
                print(e)
        elif choice == '8':
            try:
                task_id = int(input("Enter task ID to set description: "))
                description = input("Enter new description: ")
                task_manager.set_task_description(task_id, description)
                print("Task description set successfully.")
            except ValueError as e:
                print(e)
        elif choice == '9':
            keyword = input("Enter keyword to search for tasks: ")
            tasks = task_manager.search_tasks_by_keyword(keyword)
            print("Tasks matching keyword:", tasks)
        elif choice == '10':
            priority = input("Enter priority (low, medium, high) to filter tasks: ").lower()
            tasks = task_manager.filter_tasks_by_priority(priority)
            print("Tasks with priority", priority, ":", tasks)
        elif choice == '11':
            status = input("Enter status (completed/pending) to filter tasks: ").lower()
            tasks = task_manager.filter_tasks_by_status(status)
            print("Tasks with status", status, ":", tasks)
        elif choice == '12':
            deadline = input("Enter deadline (DD-MM-YYYY) to filter tasks: ")
            try:
                tasks = task_manager.filter_tasks_by_deadline(deadline)
                print("Tasks with deadline before or on", deadline, ":", tasks)
            except ValueError as e:
                print(e)
        elif choice == '13':
            print("Total number of tasks:", task_manager.count_tasks())
        elif choice == '14':
            print("Total number of completed tasks:", task_manager.count_completed_tasks())
        elif choice == '15':
            print("Total number of pending tasks:", task_manager.count_pending_tasks())
        elif choice == '16':
            summary = task_manager.generate_task_summary()
            print("Task summary:", summary)
        elif choice == '17':
            file_path = input("Enter file path to save tasks: ")
            task_manager.save_tasks_to_file(file_path)
            print("Tasks saved to file.")
        elif choice == '18':
            file_path = input("Enter file path to load tasks: ")
            task_manager.load_tasks_from_file(file_path)
            print("Tasks loaded from file.")
        elif choice == '19':
            task_manager.sort_tasks_by_deadline()
            print("Tasks sorted by deadline.")
        elif choice == '20':
            task_manager.sort_tasks_by_priority()
            print("Tasks sorted by priority.")
        elif choice == '21':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
