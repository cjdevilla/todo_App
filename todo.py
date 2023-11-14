#Create a list of task
task_list = []

def show_todo_list():
    if len(task_list) <= 0: 
        print("No task has been added so far!")

    count = 0
    for i in task_list:
        count += 1
        print(f"{count}. {i}" )    

def add_task():
    while True:
        new_task = input("Enter new task: ")
        if new_task in task_list:
            print("Task is already exists.")
            continue
        if new_task == "done":
            break
        task_list.append(new_task)
        print("Task was added.\n")

def mark_completed():
    show_todo_list()
    index = input("Enter the number of task to be completed: ")
    completed_task = int(index) - 1
    task_list.pop(completed_task)
    print("Task marked as completed \n")
    show_todo_list()

def search_task():
    search = input("Enter the task you want to search: ")
    matching_tasks = []

    for task in task_list:
        if search.lower() in task.lower():
         matching_tasks.append(task)

    if matching_tasks:
        print("Matching tasks:")
        for index in range(len(matching_tasks)):
            i = index + 1
            task = matching_tasks[index]
            print(f"{i}. {task}")

    else:
        print(f"No tasks containing '{search}' found!")

def reset_task(): 
    if len(task_list) <= 0:
        print("Nothing to clear!")
    else:
        task_list.clear()
        print("Task has been cleared!")

def options():
    while True:
        print("\n1. List down the tasks")
        print("2. Add task")
        print("3. Mark Completed")
        print("4. Search")
        print("5. Reset Task")
        print("6. Quit \n")
        choose_option = input("Choose your options (1-4): ")
        if choose_option == "1":
            show_todo_list()
        elif choose_option == "2":
            add_task()
        elif choose_option == "3":
            mark_completed()
        elif choose_option == "4":
            search_task()
        elif choose_option == "5":
            reset_task()
        elif choose_option == "6":
            print("Goodbye")
            break

options()



