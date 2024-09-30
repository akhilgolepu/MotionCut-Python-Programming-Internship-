import os

def menu():
    print("\nTo-Do List Application")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nPlease enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("\nEnter the task number to remove: "))
    if 0<task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")


tasks = []
while True:
    menu()
    choice = input("\nEnter your choice: ")
    if choice == '1':
        view_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        print("Goodbye!, Have a great day")
        break
    else:
        print("Invalid choice. Please try again.")


