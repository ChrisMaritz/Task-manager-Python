def view_mine():
    ofile_tasks = open("tasks.txt", "r+", encoding = "utf-8")
    all_tasks = ofile_tasks.read()
    all_tasks = all_tasks.split("\n")
    own_task_loop = 0
    own_task_loop2 = 0
    tasks_select = {}
    while own_task_loop < len(all_tasks):
        single_line = all_tasks[own_task_loop]

        if single_line.find(login_name) == 0:
            single_line = single_line.split(", ")
            while own_task_loop2 < len(single_line):
                adding = ','.join(single_line)
                tasks_select[own_task_loop2 + 1] = adding
                print(f"\nTask {own_task_loop2 + 1}")
                print(f"User - {single_line[0]}")
                print(f"Task title - {single_line[1]}")
                print(f"Task discription - {single_line[2]}")
                print(f"Date added - {single_line[3]}")
                print(f"Date due - {single_line[4]}")
                print(f"Task done - {single_line[5]}\n")
                single_line.pop(0)
                single_line.pop(0)
                single_line.pop(0)
                single_line.pop(0)
                single_line.pop(0)
                single_line.pop(0)   
                adding = ""
                own_task_loop2 += 1   
            all_tasks.pop(0)
        own_task_loop += 1

    select_this = 0
    select_number = 0
    ofile_tasks = open("tasks.txt", "r+", encoding = "utf-8")
    all_tasks = ofile_tasks.read()
    all_tasks = all_tasks.split("\n")
    ofile_tasks.close
    
    while select_this != -1:
        select_this = int(input("Which number tasks would you like to mark as complete?(Once you type -1 it will return to the main menu): "))
        option = input("ed - edit\ncomp - mark as complete\nWhat would you like to do: ")

        if option == "comp" and select_this != -1:
            task_single = str(tasks_select[select_this])
            task_single = task_single.split(",")
            complete_or_not = input(f"Is the task {task_single[1]} Complete?").lower()
            if complete_or_not == "yes":
                task_single[5] = "Yes"
                tasks_select[select_this] = ", ".join(task_single)
            write_loop = 0       
            while write_loop < len(all_tasks):
                if task_single in all_tasks == -1:
                    all_tasks[write_loop] = task_single
                    print(all_tasks)
                write_loop += 1
            ofile_tasks = open("tasks.txt", "w")
            all_tasks = "\n".join(all_tasks)
            ofile_tasks.write(all_tasks) 

        elif option == "ed" and select_this != -1:
            task_single = str(tasks_select[select_this]).split(",")
            if task_single[5] == "No":
                edit_which = input("usn - username\n due - Due date\nWhich one would you like to edit: ").lower()
                if edit_which == "usn":
                    change_to = input("Whats the new username?")
                    print(f"\n{usernames}")
                    if change_to in usernames:
                        task_single[0] = change_to
                        tasks_select[select_this] = ', '.join(task_single)
                    else:
                        print("That username does not exist")
                elif edit_which == "due":
                    task_single[3] = input("Whats your new due date(For example 10 Sep 2022)?: ")
                    tasks_select[select_this] = ", ".join(task_single)
                write_loop = 0       
    while write_loop < len(all_tasks):
        if task_single in all_tasks == -1:
            all_tasks[write_loop] = task_single
            print("Hello")
        write_loop += 1
                
        ofile_tasks = open("tasks.txt", "w")
        all_tasks = "\n".join(all_tasks)
        ofile_tasks.write(all_tasks)          