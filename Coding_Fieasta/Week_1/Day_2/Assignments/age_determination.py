age = int(input("Enter your Age: "))

if(age < 13):
    print("You are Child")

elif(age >= 13) and (age < 20):
    print("You are a Teenager")

elif(age >= 20) and (age < 45):
    print("You are Adult")
else:
    print("You are old")
