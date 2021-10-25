#Importing dateutil parser as well date time for use of getting current date

from datetime import date, datetime


#Opening user.txt file for user in variables.

ofile_users = open("user.txt", "r+", encoding = "utf-8")


#"read_users" first reads the "ofile_users" file then replaces each new line with a comma and space in order to be able to split each word in a list 
#"password" variable is used to store the passwords of the users
#"usernames" variable is used to store the usernames users
#number is to be used for while loop

read_users = ofile_users.read()
read_users = read_users.replace("\n", ", ")
read_users = read_users.split(", ")
password = []
usernames = []
ofile_users.close
number = 0 


#While loop loops for the length of words in the "user.txt" file.
#While doing this if the position of the word is even from 0 it will be a username and append this to variable "user_names".
#As well as if the position of word is not even from 0 it will append this to the variable "password" as it will be a password.

while number < len(read_users):

    if number % 2 == 0:
        usernames.append(read_users[number])
    else:
        password.append(read_users[number])
    number += 1

#The Booleans "correct_name" as well as "correct_password" is there to determine wether username or password is correct.
#"login_name" will be used to input the username user puts in.
#"login_password" will be used to input the password user puts in.

correct_name = False
correct_password = False
login_name = ""
login_password = ""


#While loop will carry once both "correct_name" as well as "correct_password" is true
#If the given username within the list "usernames" is correct "correct_name" will be set to True.
#If the given password within the list "password" is correct "correct_password" will be set to True but this input will only come up if username is True.
#If the given username within the list "usernames" is incorrect "correct_name" will be set to False.
#If the given password within the list "password" is incorrect "correct_password" will be set to False.

while correct_name == False or correct_password == False:
    login_name = input("Please enter your username(if this appears again your login name or password does not exist): ")
    if login_name in usernames:
        correct_name = True
    else:
        correct_name = False

    if correct_name == True:
        login_password = input("Please enter your password(if this appears again your login name or password does not exist): ")
        if login_password in password:
            correct_password = True
        else:
            correct_password = False


#"password_confirmed" variable is used to confirm the password for a new registered user.
#"options" variable is for the input of user to confirm which option they select.

password_confirmed = False
options = ""
ofile_tasks = open("tasks.txt", "a")


#The function "reg_user()"" is created, the purpose of this function is to register a new user.
#The variable "password_confirmed" is a boolean which will be used to confirm the user types in the correct password when registering a user.
#A while loop is created which will run till "password_confirmed" is set to True; meaning once it is True the password has been typed in twice correctly.
#An input "new_password" is created which functions as the password the admin wants for the user they are registering.
#"confirm_password" variable functions as an input for the user to type in their password again to see if they have the one the require.
#An if else statement will determine wether the password has been confirmed; if it is correct the variable "password_confirmed" will be set to True.
#Once "password_confirmed" is set to True it open the "user.txt" file and write the new username("new_username") and new password("new_password") to the file storing the needed info.

def reg_user():
    new_username = (input("Please enter the username: "))
    while new_username in usernames:
        if new_username in usernames:
            print("This user already exists; please try again.")
            new_username = (input("Please enter the username: "))

    password_confirmed = False
    while password_confirmed == False:
        new_password = input("Please enter password (if this appears again your password was not confirmed): ")
        confirm_password = input("Please confirm password: ")
        if confirm_password == new_password:
            password_confirmed = True
        else:
            password_confirmed = False

        if password_confirmed == True:
            ofile_users = open("user.txt", "a")
            ofile_users.write("\n"+ new_username + ", " + new_password)
            ofile_users.close     


#The function "add_task" is created here; this function serves as a purpose to add a task to the user you choose.
#Within the task the "task.txt" file is opened in appending mode as to allow each seperate task to be on a new line with no complications.
#The Boolean value set to false "user_task_exist" is there to serve the purpose as to make sure the username entered indeed does exist.
#The While loop will run until "user_task_exist" is set to True but it is worth mentioning although it set to True within the while loop that just means it wont run a second time once its done with that code block.
#an input is asked called "user_task" which is to ask which user a task is assigned to.
#If that input exists as a username The if statement will run resulting in "user_task_exist" to be set to True.
#It will then ask for the needed details(inputs) for the form being:
#"task_title"; the tasks title.
#"task_discrip"; the discription of the task.
#"due_date"; the date that the task is due.
#"task_complete";(not an input) Which serves as a purpose to inform that the the task is complete, this is automatically set to "No".
#"current"; (not an input) to show what date the task is assigned on.
#And then finally after all this all the needed info is written in the appropiate form in "task.txt" being "ofile_tasks" 

def add_task():
    ofile_tasks = open("tasks.txt", "a")
    user_task_exist = False

    while user_task_exist == False:
        user_task = input("Which user do you choose: ")
        if user_task in usernames:
            user_task_exist = True
            task_title = input("What is the task title: ")
            task_discrip = input("Give a discription of the task: ")
            due_date = input("What is the due date? (For example 10 Sep 2022): ")
            task_complete = "No"
            current = datetime.today().strftime("%d %b %Y")
            ofile_tasks.write("\n" + user_task + ", " + task_title + ", "  + task_discrip + ", " + current + ", " + due_date + ", " + task_complete )
            ofile_tasks.close()


#A function called view_all is created here for purpose of presenting all the tasks that are input in the appropiate manner.
#"ofile_tasks" variable opens the file which is closed just before the while loop. 
#After this the open file is read to the variable all_tasks.
#Each new line in "all_tasks" is then replaced with a comma and space as this will be used as a seperator for when it is created into a list.
#"all_tasks" is "split()" into a list seperated by a comma and a space as a list will be practical for the intended use.
#A variable "task_loop" is created intended for the use of a while loop for it to be iterated.
#A while loop is then created which will run while the iterated variable is less than the length of all the tasks.
#Each time the loop run it will print each item consecutively in the order needed for example "User" being the first task in the list and "Task title" being the next etc.
#Then 6 items are taken off the list being which is needed for the each single tasks details allowing the same operation to be done for the next task.

def view_all():
    ofile_tasks = open("tasks.txt", "r+", encoding = "utf-8")
    all_tasks = ofile_tasks.read()
    all_tasks = all_tasks.replace("\n", ", ")
    all_tasks = all_tasks.split(", ")
    task_loop = 0
    ofile_tasks.close()

    while task_loop < len(all_tasks):
        print(f"\nUser - {all_tasks[0]}")
        print(f"Task title - {all_tasks[1]}")
        print(f"Task discription - {all_tasks[2]}")
        print(f"Date added - {all_tasks[3]}")
        print(f"Date due - {all_tasks[4]}")
        print(f"Task done - {all_tasks[5]}")
        all_tasks.pop(0)
        all_tasks.pop(0)
        all_tasks.pop(0)
        all_tasks.pop(0)
        all_tasks.pop(0)
        all_tasks.pop(0)
        task_loop += 1


#A function named "view_mine" is created here which serves the purpose of specifically viewing the logged in users tasks.
#Within the function the "tasks.txt" file is open within the variable "ofile_tasks" which is then read and applied to the variable "all_tasks"
#The tasks within "all_tasks" is the "split()" into a list seperated by each line.
#A variable called "counted" is created which is equal to 0
#A for loop is created which goes through each item in "all_tasksS"
#If the login name is found within the line in the for loop the following will be done.
#"single_line" is the split() by each item which is seperated by ", "
#Each item in "single_line" is then printed with the needed discriptions
#Then counted is enumurated then the for loop is exited.
#"complete_edit" asks wether the user would like to modify a task and if yes is entered then "complete_task()" will be called.

def view_mine():
    ofile_tasks = open("tasks.txt", "r+", encoding = "utf-8")
    all_tasks = ofile_tasks.read()
    all_tasks = all_tasks.split("\n")
    
    counted = 0
    for line in all_tasks:
        if line.find(login_name) == 0:
            single_line = line.split(", ")
            print(f"\n Task {counted + 1}")
            print(f"User - {single_line[0]}")
            print(f"Title - {single_line[1]}")
            print(f"Discription - {single_line[2]}")
            print(f"Date added - {single_line[3]}")
            print(f"Date due - {single_line[4]}")
            print(f"Task done - {single_line[5]}\n")
        counted += 1
    
    complete_edit = input("Would you like to modify a task(yes or no): ")
    if complete_edit == "yes":
        complete_task()


#"complete_task()" funnctions to mark a task as complete or to edit a tasks username or due date.
#First "tasks.txt" is created and stored in "ofile_tasks"
#The text file is the read to "tasks_read" and split by each new line.
#"counted" is created and set to 0.
#A for loop is then created which goes through each line stored in "tasks_read".
#"single_list" is then created and is equal to the single line split by ", " thus storing each item in the line.
#An if statment is then created which checks if "single_list" is empty as an error was coming up because the loop would do this.
#Each item in "single_list" is displayed with the proper info with the exception of the first one which is "counted" + 1 as this will number each list item apporopiatly.
#counted is then enumurated as to number each task.
#"which_task" is an input which asked which task the user wants to select minused by 1 as the item itself started at 0.
#"selected_task" is equal to the task item the user selects.
#"complete_edit" is an input which is to ask the user wether they want to edit or mark a task complete.

def complete_task():

    ofile_tasks = open("tasks.txt", "r+", encoding = "utf-8")
    tasks_read = ofile_tasks.read()
    tasks_split = tasks_read.split("\n")
    counted = 0

    for line in tasks_split:
        single_list = line.split(", ")
        if single_list != [""]:
            print(f"\n Task {counted + 1}")
            print(f"User - {single_list[0]}")
            print(f"Title - {single_list[1]}")
            print(f"Discription - {single_list[2]}")
            print(f"Date added - {single_list[3]}")
            print(f"Date due - {single_list[4]}")
            print(f"Task done - {single_list[5]}")
    
        counted += 1

    which_task = int(input("Which tasks would you like to mark as edit or mark complete from the list above?(-1 will return to main menu): ")) - 1
    selected_task = str(tasks_split[which_task])
    selected_task = selected_task.split(", ")
    complete_edit = input("Would you like to edit or mark a tasks as complete?\n edit - ed\nmark complete - comp\nenter here: ")


    #If the user inputs "comp" the following will be done.
    #The fifth item in "selected_task" is then replaced by "Yes"
    #The chosen task in "tasks_split" is then replaced by the newly edited one of it being "selected_task"
    #"tasks.txt" is then opened and the new data is writted with "tasks_split" is made into a string using join() then the file is closed.

    if complete_edit == "comp":
        selected_task[5].replace("No", "Yes")
        tasks_split[which_task] = f"{selected_task[0]}, {selected_task[1]}, {selected_task[2]}, {selected_task[3]}, {selected_task[4]}, Yes"
        ofile_tasks = open("tasks.txt", "w")
        ofile_tasks.write("\n".join(tasks_split))
        ofile_tasks.close
    

    #If "ed" is entered the following will be done.
    #"usr_due" asks the user wether they want to edit the username or due date.
    #if "usr" is entered within "usr_due" the following will happen.
    #First the new username is asked for and saved in "new_name"
    #if "new_name" is found in "usernames" the following will happen.
    #the first item in "selected_task" is replaced by "new_name" thus replacing the old username with the new one.
    #The chosen task is then changed with the new input.
    #The task is then opened in "w" so the new information can replace the old information.
    #The new tasks are then written to the file and made into a string with join() and the file is closed.
    #If "new_name" does not exist in usernames it will print "That user does not exist".

    elif complete_edit == "ed":
        usr_due = input("Would you like to edit the username or due date\nusername - usr\ndue date - due\nenter here: ")

        if usr_due == "usr":
            new_name = input("What is the new username: ")
            if new_name in usernames:
                selected_task[0].replace(login_name, new_name)
                tasks_split[which_task] = f"{new_name}, {selected_task[1]}, {selected_task[2]}, {selected_task[3]}, {selected_task[4]}, {selected_task[5]}"
                ofile_tasks = open("tasks.txt", "w")
                ofile_tasks.write("\n".join(tasks_split))
                ofile_tasks.close
            else:
                print("That user does not exist")


        #An if else statmented for "usr_due" is then created checking if the user inputs "due" instead of "ed"
        #"new_date" is then created asking for the due date they want to put in.
        #the 4th item in selected_task is then replaced with "new_date"
        #The chosen task in "tasks_split" is then modified and the new date is then put in
        #The task is then opened in "w" so the new information can replace the old information.
        #The new modified tasks are then written into the file and the file is closed.

        elif usr_due == "due":
            new_date = input("What is your new due date(for example: 20 Sept 2021): ")
            selected_task[4].replace(selected_task[4], new_date)
            tasks_split[which_task] = f"{selected_task[0]}, {selected_task[1]}, {selected_task[2]}, {selected_task[3]}, {new_date}, {selected_task[5]}"
            ofile_tasks = open("tasks.txt", "w")
            ofile_tasks.write("\n".join(tasks_split))
            ofile_tasks.close
    

#"overview_tasks()" is made to create a txt file with all the needed details about the tasks.
#First the variables "tasks_amount", "tasks_incomp", "tasks_comp", "past_due" is created all set to 0.
#Next a date object is created which and formatted to a cerrian format.
#"tasks.txt" is then opened in "ofile_tasks" and read to "tasks_read" and split seperated by each new line.
#A for loop is then created which goes through each line thus going through each task.
#"line_list" is then created split by a ", " and a variable "date" is made choosing the due date of the task and creating it into a date object.
#If "No" is found in "line_list" "tasks_incomp" is enumrated thus storing the amount if incomplete tasks.
#Within this if statement another if statement is created which check if the due date is less then the current date which will then enumarate "past_due" storing the amount of over due tasks that are not complete.
#If "No" is not found an else if statement will check if "Yes" is found and if it is "tasks_comp" will be enumurated thus storing all the complete tasks.
#The variable "tasks_amount" is then enumurated thus storing the amount tasks.
#Outside of the loop "percent_incomp" is created which calculated the percent of incomplete tasks.
#Then "percent_ovrdue" is created which calculates the percent of overdue tasks
#"task_overview.txt" is opened in "w" as incase it is created already so it can input the new data.
#All the needed info is then written in the file in a neat format and then the file is closed.

def overview_tasks():

    tasks_amount = 0
    tasks_incomp = 0
    tasks_comp = 0
    past_due = 0
    current_date = datetime.today()
    current_date = datetime.strftime(current_date, "%d %b %Y")
    current_date = datetime.strptime(current_date, "%d %b %Y")
    ofile_tasks = open("tasks.txt", "r+", encoding = "utf-8")
    task_read = ofile_tasks.read()
    task_read = task_read.split("\n")
    ofile_tasks.close()
    
    for line in task_read:
        line_list = line.split(", ")
        date = line_list[4]
        date = datetime.strptime(date, "%d %b %Y")
        if "No" in line_list:
            tasks_incomp += 1
            if date < current_date:
                past_due += 1
        elif "Yes" in line_list:
            tasks_comp += 1

        tasks_amount += 1

    percent_incomp = tasks_incomp / tasks_amount  * 100
    percent_ovrdue = past_due / tasks_amount * 100

    ofile_over_task = open("task_overview.txt", "w")
    ofile_over_task.write(f"Number of tasks : {tasks_amount}\nnumber of completed tasks : {tasks_comp}\nnumber of incompleted tasks : {tasks_incomp}\noverdue : {past_due}\npercentage incomplete : {int(percent_incomp)}%\npercent overdue : {int(percent_ovrdue)}%")
    ofile_over_task.close
        

#"overview_user()" functions as a function to create a text file with all the users data regarding the tasks.
#The first block of code the "user.txt" fil is opened and read to "users_read" and the split into a list seperated by each new line and then the file is closed again which is assigned to "ofile_users"
#Next the exact same process is done again except just with "tasks.txt" instead of "user.txt"
#Next a list is made assigned to the variable "users_amount" which is then used and counted in a for loop which goes through each item in "user_read" which is each line in "user.txt" thus counting the amount of users.
#Next the dictionary "user_report" is created outside the upcoming loop as this is the only loop we dont want to reset.
#The first loop after "user_report" goes through each username stored in "usernames"
#Next the variables "comp" "still_comp" "usr_task_amount" "usr_due" "tasks_amount" is created and will be elaborated on.
#"current_date" is made which is a date object on the present date.
#The next for loop is created which goes through each task in "tasks.txt"
#"tasks_amount" is enumarated each as this will store the amount of tasks.
#"line_list" is created which is a list of each item of a single task line.
#An if statment checks if the current username in the first loop is in "line_list"
#Then "tasks_amount" is enumarated and a date object is created from the item in the list which is the due date and stored in "date"
#If the string "No" is found in "line_list" "still_comp" is enumurated which is the tasks which are not completed.
#Within that if statement if "date" is less than "current_date" "usr_due" will be enumurated which is the amount of tasks past due date and not complete.
#An if else statement is made which if "Yes" is found in "line_list" "comp" is enumarated storing all the completed tasks.
#the second for loop is then exited keeping in mind we are still in the usernames for loop.
#several if else statements are created so that there will be no errors in attempting to divide by zero.
#an item in "user_report" is then created which is named the username in the for loop and a dictionary is then applied to that item with all the needed info stored neatly.

def overview_user():

    ofile_users = open("user.txt", "r+", encoding = "utf-8")
    users_read = ofile_users.read()
    users_read = users_read.split("\n")
    ofile_users.close()
    ofile_tasks = open("tasks.txt", "r+", encoding = "utf-8")
    task_read = ofile_tasks.read()
    task_read = task_read.split("\n")
    ofile_tasks.close()

    users_amount = 0
    for line1 in users_read:
        users_amount += 1

    user_report = {}
    for line2 in usernames:
        comp = 0
        still_comp = 0
        usr_task_amount = 0
        usr_due = 0
        tasks_amount = 0
        current_date = datetime.today()
        current_date = datetime.strftime(current_date, "%d %b %Y")
        current_date = datetime.strptime(current_date, "%d %b %Y")
        for line3 in task_read:
            tasks_amount += 1
            line_list = line3.split(", ")
            if line2 in line_list:
                usr_task_amount +=1
                date = line_list[4]
                date = datetime.strptime(date, "%d %b %Y")  
                if "No" in line_list:
                    still_comp += 1
                    if date < current_date:
                        usr_due += 1
                elif "Yes" in line_list:
                    comp += 1
            
        if comp == 0:
            percent_comp = 0
        else:
            percent_comp = int(comp / usr_task_amount * 100)
        
        if still_comp == 0:
            percent_still = 0
        else:
            percent_still = int(still_comp / usr_task_amount * 100)

        if usr_due == 0:
            due_percent = 0
        else:
            due_percent = int(usr_due / usr_task_amount * 100)
                
        user_report[line2] = {"user" : line2, "complete" : comp, "not complete" : still_comp, "tasks amount" : usr_task_amount, "over due" : usr_due, "percent not due" : due_percent, 
        "percent not" : percent_still, "percent complete" : percent_comp}


    #"user_overview.txt" is opened in "w" as to clear all data incase it is being updated instead of created.
    #it is closed then opened in "a" and first the amount of users and tasks amount is written into the file.
    #A for loop is then created which goes through each username and writed all the needed information in the txt file and after the loop the file is closed again.

    ofile_usr_over = open("user_overview.txt", "w")
    ofile_usr_over.close
    ofile_usr_over = open("user_overview.txt", "a")
    ofile_usr_over.write(f"amount of user : {users_amount}, task amount : {tasks_amount}")
    for user in usernames:
        ofile_usr_over.write(f"\nuser : {user_report[user]['user']}, completed : {user_report[user]['complete']}, not complete : {user_report[user]['not complete']}, tasks : {user_report[user]['tasks amount']}, over due : {user_report[user]['over due']}, percent over due : {user_report[user]['percent not due']}, percent incomplete : {user_report[user]['percent not']}, percent complete : {user_report[user]['percent complete']}")
    ofile_usr_over.close

#This function simply functions as it can be called so both "overview_user" and "overview_tasks" can be called the same time.

def task_user_overview():
    overview_user()
    overview_tasks()


#The function "stats()" is created here. This will function as a way to view all the needed stats within "user_overview.txt" and "task_overview.txt".
#the first thing in the function "task_user_overview()" is called incase the txt files needed are not created yet.
#"ofile_usr_over" opens "user_overview.txt" in "r" mode and then this file is read in "usr_over_read".
#Each new line is replaced with ", " and then it is split by each ", "

def stats():
    task_user_overview()
    ofile_usr_over = open("user_overview.txt", "r")
    usr_over_read = ofile_usr_over.read()
    usr_over_read = usr_over_read.replace("\n", ", ")
    usr_over_read = usr_over_read.split(", ")
    ofile_usr_over.close()

    #"user_items" is created which is an empty list.
    #A for loop is then created which goes over each line in "user_overview.txt.txt"
    #Item is equal to each item in "over_task_read" without the discriptions and etc
    #"item" is then appended to user_items.


    user_items = []
    for line in usr_over_read:
        #In the line below I was struggling to find a way to get each item from the file without the discriptions etc
        #I found a solution here https://stackoverflow.com/questions/35162922/python-slice-string-by-character-and-not-index/45316415 and edited and used it accordingly.
        #Instead of printing like in the solution given I assigned it to a variable then appending it into a list as well as implementing it in a for loop.
        item = line.split(" : ")[1]
        user_items.append(item)
    

    #"task_overview.txt" is opened in ofile_task_over.
    #It is then read in "over_task_read" and split by each new line.
    #"task_items" is created which is an empty list.
    #A for loop is then created which goes over each line in "task_overview.txt"
    #Item is equal to each item in "over_task_read" without the discriptions and etc
    #"item" is then appended to task_items.

    ofile_task_over = open("task_overview.txt", "r")
    over_task_read = ofile_task_over.read()
    over_task_read = over_task_read.split("\n")
    ofile_task_over.close()
    task_items = []
    for line in over_task_read:
        item = line.split(" : ")[1]
        task_items.append(item)
    

    #The first two items in "user_items" is printed and then popped off the list because if it was in the list it would complicate the upcoming for loop.

    print(f"\nUser stats\nTotal users : {user_items[0]}\nTotal tasks {user_items[1]}")
    user_items.pop(0)
    user_items.pop(0)


    #A for loop is created which goes over each item in "user_items"
    #Each detail of each user is printed with the needed discription then popped to make way for the next users details and then the same is done.

    
    for data in user_items:
        print(f"\nuser '{user_items[0]}' data")
        print(f"Number of completed tasks : {user_items[1]}")
        print(f"Tasks not complete : {user_items[2]}")
        print(f"Total tasks : {user_items[3]}")
        print(f"Tasks over due and not complete : {user_items[4]}")
        print(f"Percent of tasks overdue : {user_items[5]}%")
        print(f"Percent of tasks incomplete : {user_items[6]}%")
        print(f"Percent of tasks complete : {user_items[7]}")
        user_items.pop(0)
        user_items.pop(0)
        user_items.pop(0)
        user_items.pop(0)
        user_items.pop(0)
        user_items.pop(0)
        user_items.pop(0)
        user_items.pop(0)
    

    #All the data from "task_items" is then printed with the needed discriptions.


    print("\nTasks data ")
    print(f"Total number of Tasks : {task_items[0]}")
    print(f"Completed tasks : {task_items[1]}")
    print(f"Incompleted tasks : {task_items[2]}")
    print(f"Over due tasks : {task_items[3]}")
    print(f"Percentage incomplete : {task_items[4]}")
    print(f"Percentage Past Due : {task_items[5]}\n")

        
#If the user succesfully logs in this if conditional will work as show with "correct_password" as well as "correct_name"
#list of options given to user to decide what they would like to do; depending on what they type it will do what they request.
#if "r" is selected it will call the function "reg_user()" with teh argument of an input of which is what user the admin would like to register. This is where the username is entered for the function.
#If the login is not the admin a prompt will appeared informing that the user logged in is not the admin.

if correct_password == True and correct_name == True:
    while options != "e":
        options = input("Please select one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\nstats - view statistics\ngr - generate reports\ne - exit\nenter here: ").lower()

        if options == "r" and login_name == "admin":
            reg_user()
        elif options == "r" and login_name != "admin":
            print("You are not the admin.")


#If the user types in a standing for "add task" the function add_task will be called which function as assigning tasks for the needed user.

        elif options == "a":
            add_task()


#If "va" is selected the function "view_all" is called which functions as displaying all the tasks needed.

        elif options == "va":
            view_all()


#If "vm" is selected the funtion "view_mine" is called which funtions as displaying all the logged in users tasks.

        elif options == "vm":
            view_mine()


#If "stats" is selected the function "stats()" will be called functioning as a way to view the stats of all the info in "user_overview.txt" an "task_overview.txt"

        elif options == "stats":
            stats()

#If "gr" is selected the function "gen_reports" will be called.

        elif options == "gr":
            task_user_overview()