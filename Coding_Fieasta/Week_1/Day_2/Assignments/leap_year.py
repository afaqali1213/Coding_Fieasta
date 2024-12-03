year = int(input("Enter the Year: "))

if(year % 4 == 0 or year % 400 == 0):
    print("It's a Leap Year")
else:
    print("It's not a leap year")
