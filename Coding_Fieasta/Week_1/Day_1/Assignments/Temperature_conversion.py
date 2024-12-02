# Temperature Conversion

user_selection = int(input("What do you want to do?\n1) Celsius to Fahrenheit\n2) Fahrenheit to Celsius\nEnter number(1-2): "))

if (user_selection == 1):
    temp_in_C = int(input("Enter Temperature in Celsius: "))
    temp_in_F = (temp_in_C*1.8)+32
    print(f"{temp_in_C}°C in Fahrenhiet is {temp_in_F}°F")


elif(user_selection == 2):
    temp_in_F = int(input("Enter Temperature in Fahrenheit: "))
    temp_in_C = (temp_in_F-32)*5/9
    print(f"{temp_in_F}°F in Celsius is {temp_in_C}°C")
end = True
