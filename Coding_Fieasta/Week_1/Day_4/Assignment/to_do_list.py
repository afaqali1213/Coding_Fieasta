task = dict()
completed_task = dict()

while True:
   x = int(input("""\bWelcome to the Shopping List\b
         Select the function you want to perform:
         1) Add New Task
         2) Mark as Complete
         3) Pending Task
         4) Exit       
                   
          Enter your Selection """))
   if x >= 5:
       print("Please Enter the number Specified with the operation")
   

   if x == 1:
       task_name = input("Enter name of Task: ").capitalize()
       due_date = input("Enter the due date of Task: ")
       task[task_name]= due_date
       print(f"The task {task_name} has been Added")

   elif x == 2:
       task_name = input("Enter the task name you want to mark as completed: ").capitalize()
       task.pop(task_name)
       completed_task[task_name]= due_date
       print("Here's list of completed tasks",completed_task)

   elif x == 3:
       print("The pending tasks are: ",task)

   elif x == 4:
       print("Thanks!")
       break