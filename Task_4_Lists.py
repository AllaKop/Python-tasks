# Program that manages a simple to-do list. 
# Implement options to add tasks, view the list, and mark tasks as completed.
# Use a list to stor tasks.

to_do_list = []

while True:
    your_choice = int(input("Enter a number wich corresponds your choice: 1: Add Task 2: View List 3: Remove Task 4: Exit -  "))

    if your_choice == 1:
        task = str(input("Write a name of the task to add "))
        to_do_list.append(task)
    elif your_choice == 2:
        print("To-do List: ", to_do_list)
    elif your_choice == 3:
        task = str(input("Write a name of the task to remove "))
        if task in to_do_list:
            to_do_list.remove(task)
        else: 
            raise Exception("Task {task} is not in the list.")
    elif your_choice == 4:
        break
    else:
        raise Exception("Wrong option. Please enter a number wich corresponds your choice: 1: Add Task 2: View List 3: Remove Task 4: Exit ")
