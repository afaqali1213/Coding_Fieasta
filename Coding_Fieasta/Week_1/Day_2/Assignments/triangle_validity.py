print("\'Enter the three sides of Triangle\'")

first_side = int(input("Length of 1st Side: "))
second_side = int(input("Length of 2nd Side: "))
third_side = int(input("Length of 3rd Side: "))

if((first_side + second_side) > third_side):
    print("It's a Valid Triangle")

elif((third_side + second_side) > first_side):
    print("It's a Valid Triangle")

elif((first_side + third_side) > second_side):
    print("It's a Valid Triangle")

else:
    print("It's not a Valid Triangle")

