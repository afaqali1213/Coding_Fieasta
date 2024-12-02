# Quadratic Equation Solver

import math

a = int(input("Enter the 'a' element of Quadratic Equation: "))
b = int(input("Enter the 'b' element of Quadratic Equation: "))
c = int(input("Enter the 'c' element of Quadratic Equation: "))

x1 = (-b+math.sqrt(b**2-(4*a*c)))/2*a
x2 = (-b-math.sqrt(b**2-(4*a*c)))/2*a

print("The solution set is ")
print({x1,x2})


# Circle Measurement

r = int(input("Enter radius of Circle: "))

area = math.pi*(r**2)
print(f"Area of Circle is {area}")
