obtained_marks = int(input("Enter your Obtained Marks: "))

total_marks = int(input("Enter your Total Marks: "))

percentage = (obtained_marks/total_marks)*100


if(percentage <= 100 and percentage >= 90):
    print(f"Congrats! You got A+ Grade and Your Percentage is {percentage}")

elif(percentage < 90 and percentage >= 85):
    print(f"You Got A Grade and Your percentage is {percentage}%")

elif(percentage < 85 and percentage >= 75):
    print(f"You got B Grade and Your Prcentage is {percentage}%")

elif(percentage < 75 and percentage >= 70):
    print(f"You got C Grade and Your Prcentage is {percentage}%")

elif(percentage < 70 and percentage >= 60):
    print(f"You got D Grade and Your Prcentage is {percentage}%")

elif(percentage < 60 and percentage >= 50):
    print(f"You got E Grade and Your Prcentage is {percentage}%")

else:
    print("Work Hard!")