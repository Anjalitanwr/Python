def task():
    tasks =[]
    print("Welcome to my Task manaagement App")

    total_task = int(input("Enter how many task you want to add ="))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {1}=")
        tasks.append(task_name)
    print("Today's Tasks are\n{tasks}")

    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/"))
        if operation ==1:
            add=input("Enter task you want to add=")
            tasks.append(add)
            print(f"Task {add} has been successfully added... ")

        elif operation ==2:
            update_val = input("Enter the task name you want to update=")
            if update_val in tasks:
                up = input("Enter new task=")
                ind= tasks.index(update_val)
                tasks[ind]=up
                print(f"Update task{up}")
        
        elif operation ==3:
            del_val = input("which task you want to delete=")
            if del_val in tasks:
                ind= tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted....")

        elif operation ==4:
            print(f"Total tasks = {tasks}")

        elif operation ==5:
            print("closing the program.....")
            break

        else:
            print("invalid input")
      

task()

