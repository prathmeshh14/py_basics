lst=[]

def input_tasks():
    n=int(input("Enter the number of tasks:"))
    for i in range(n):
        task = input(f"Enter task {i + 1}: ")
        lst.append({"task": task, "completed": False})
    display_tasks()
    Extra=input("Do you want to perform any action? (y/n): ")
    if Extra.lower()=="y":
        return True
    else:
        return False

def display_tasks():
    print("tasks:")
    for i,task in enumerate(lst,start=1):
        print(f"{i}. {task['task']} - {'Completed' if task['completed'] else 'Not Completed'}")


def mark_task_completed():
    display_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(lst):
        lst[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def delete_task():
    display_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(lst):
        deleted_task = lst.pop(task_number - 1)
        print(f"Task '{deleted_task['task']}' deleted.")
    else:
        print("Invalid task number.")

def edit():
    display_tasks()
    task_number= int(input("Enter the task number to edit: "))
    if 1<= task_number <=len(lst):
        new_task=input("Enter the new task description: ")
        lst[task_number - 1]["task"]=new_task
        print(f"Task {task_number} updated.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Input tasks")
    print("2. Display tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Edit task")
    choice=input("Enter your choice : ")
    match choice:
        case "1":
            input_tasks()
        case "2":
            display_tasks()
        case "3":
            mark_task_completed()
        case "4":
            delete_task()
        case "5":
            edit()
        case _:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")