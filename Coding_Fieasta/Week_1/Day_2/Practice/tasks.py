# # Task 1

# a = 4

# if(a== 3):
#     print("a is equal to 3")
# else:
#     print("a is not equal to 3")

# # Task 2

# num = int(input("Enter any number: "))

# if(num%2 == 0):
#     print("It's an Even Number")
# else:
#     print("It's an Odd Number")


# Task 3
salary = int(input("Enter your Salary Amount: "))

if(salary < 600000 ):
    print("No Tax")

elif(salary > 600000 and salary < 1200000 ):
    tax = 0.05*(salary-600000)
    print("Your Tax for the year will be: ",tax)

elif(salary > 1200000 and salary < 2200000 ):
    tax = 0.15*(salary-600000) + 30000
    print("Your Tax for the year will be: ",tax)

elif(salary > 2200000 and salary < 3200000 ):
    tax = 0.25*(salary-600000) + 180000
    print("Your Tax for the year will be:",tax)


# Task 4

rates = (0.05, 0.15, 0.25, 0.3)
