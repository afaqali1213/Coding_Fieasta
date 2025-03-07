# Validate user_input

class Person:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.set_name(name)
        self.set_age(age)
    
    

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if not value.isalpha():
            raise TypeError("Enter Valid Name!")
        
        self._name = value

    def get_age(self):
        return self._age
    
    def set_age(self, num):
        if not isinstance(num, int):
            raise ValueError("The age must be a number")
        if num <= 0:
            raise ValueError("The age should be a positive integer")
        self._age = num

try:
    
    person = Person("Afaq",26)
    print(person.get_name())
    print(person.get_age())

except ValueError as e:
    print("Error:",e)


# Product Price Validation

class Product:
    def __init__(self, name, price):
        self._name = None
        self._price = None
        self.set_name(name)
        self.set_price(price)

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if not value.isalpha():
            raise TypeError("Invalid Product Name")
        

    def get_price(self):
        return self._price
    
    def set_price(self, value):
        if not isinstance(value, int):
            raise ValueError("Enter an Integer")      

product = Product("Table", 1200)
print(product.get_name())


# Division Program With Exception Handling
x = int(input("Enter any Number: "))
y = int(input("Enter any Number: "))

try:
    print(x/y)
except ValueError as v:
    print(f"Error: {v}")

except ZeroDivisionError as d:
    print("Division by Zero is not Allowed")


# Student Grades Management

class Student:
    grades = list()
    def __init__(self, grades= None):
        if grades is None:
            grades = []

        self.set_grades(grades)


    def get_grades(self):
        return self._grades
    
    def set_grades(self, value):
        if not isinstance(value, list):
            raise TypeError("Grades should be in List format")
        for val in value:
            if not ( 0 < val <= 100):
                raise ValueError(f"Invalid Grade: {val}. Grades must be between 1 and 100")
    
        self._grades = value
    grades = property(get_grades, set_grades)
try:
    student = Student([85, 90, 78])  # Valid grades
    print("Grades:", student.grades)  # Access grades via the property

    student.grades = [95, 88, 102]  # Invalid grade (102)
except ValueError as e:
    print("Error:", e)


# Data from file

file_name = input("Enter a file name: ")

try:
   with open(file_name, 'r') as file:
      print(file.read())

except FileNotFoundError:
    print(f"The file with the name '{file_name}' doesn't exist")
except Exception as e:
    print("Unexpected error Occured:",e)

