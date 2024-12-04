num = input("Enter number: ")

sum = 0
for i in num:
    sum += int(i)**3


if sum == int(num):
    print("It's an Armstrong Number")
else:
    print("It's not an Armstrong Number")

