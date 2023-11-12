#Create a list of task
task_list = []

def show_todo_list():
    count = 0
    for i in task_list:
        count += 1
        print(f"{count}. {i}" )    

def add_task():
    while True:
        new_task = input("Enter new task: ")
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

def options():
    while True:
        print("\n1. List down the tasks")
        print("2. Add task")
        print("3. Mark Completed")
        print("4. Quit \n")
        choose_option = input("Choose your options (1-4): ")
        if choose_option == "1":
            show_todo_list()
        elif choose_option == "2":
            add_task()
        elif choose_option == "3":
            mark_completed()
        elif choose_option == "4":
            print("Goodbye")
            break

options()



