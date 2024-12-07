operation_list = list()

while True:
   x = int(input("""\bWelcome to the Calculator\b
         Select the function you want to perform:
         1) Addition
         2) Subtraction
         3) Multiplication
         4) Division
         5) Exit
                   
          Enter Operation number: """))
   

   if x == 1:
       n1 = int(input("Enter a number: "))
       n2 = int(input("Enter the second number: "))
       sum = n1 + n2
       print("Solution of Sum is:",sum)
       operation_list.append("Addition")

   elif x == 2:
       n1 = int(input("Enter a number: "))
       n2 = int(input("Enter the second number: "))
       subtraction = n1-n2
       print("Solution of Subtraction is:", subtraction)
       operation_list.append("Subtraction")

   elif x == 3:
       n1 = int(input("Enter a number: "))
       n2 = int(input("Enter the second number: "))
       product = n1*n2
       print("Solution of Division is:", product)
       operation_list.append("Multiplication")
    
   elif x == 4:
       n1 = int(input("Enter a number: "))
       n2 = int(input("Enter the second number: "))
       if n2 == 0:
           print("Division by Zero is not Allowed")
       
       division = n1/n2
       print("Solution of Division is:", division)
       operation_list.append("Division")
       

   elif x == 5:
       print("Thanks for using Calculator. The operation you performed are:",operation_list)
       break
