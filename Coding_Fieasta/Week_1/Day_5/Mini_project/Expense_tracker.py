expense = dict()

while True:
  print("Welcome to personal Expense Tracker")
  print("""
      1) Add Expense
      2) View All Expense
      3) View Totals and Averages
      4) Exit""")
  
  x = int(input("Choose an option: "))


  if x == 1:
       expense_name = input("Enter description: ").capitalize()
       expense_amount = int(input("Enter Amount: "))
       expense[expense_name]= expense_amount
       print("Expense Added Successfully!")

  elif x ==2:
       for key,value in expense:
           print(f"{key} - {value}Rs.")

  elif x ==3:
       sum = 0
       for value in dict:
           sum += value
           print("The sum of Expenses=",sum)
           

  elif x == 4:
       print("Thanks!")
       break