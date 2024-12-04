num = int(input("Enter any number: "))


for i in range(1, num+1):
    if num / i != 0:
        print("It's not a prime number")
    else:
        print("It's prime number.")
