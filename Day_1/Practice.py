from pprint import pprint
# #     OOP in Python

# class Student:
#     #Default Constructor
#     def __init__(self):
#         pass

#     # Parameterized Constructor
#     semester = "3rd Semester" # Class Attribute
#     name = "N/A"
#     def __init__(self, name, marks):  # The self parameter is a reference
#         print("Adding new students in Database...")
#         self.name = name   # Object attribute
#         self.marks = marks

# # The variable after the . can be different but not after the = sign


# s1 = Student("Afaq", 56)
# print(s1.semester)
# print(s1.name)

# s2 = Student("Rizwan", 50)
# pprint(vars(s2))
# print(s2.semester)

# class Car():

#     def __init__(self):
#         self.color = "Blue"
#         self.brand = "Honda"
#         self.model = 2023
#         self.a = "nothing"

# car1 = Car()
# pprint(vars(car1)) # return the output in the form of dict also sort alphabetically

# Class & Instance Attributes

# Class.attr
# If I have a Class with the name student. They can have different names.


# Methods

# Class has attributes and Methods
# Methods are basically functions that belongs to the objects 

class Student:
    #Default Constructor
    def __init__(self):
        pass

    # Parameterized Constructor
    semester = "3rd Semester" # Class Attribute
    name = "N/A"
    def __init__(self, name, marks):  # The self parameter is a reference
        print("Adding new students in Database...")
        self.name = name   # Object attribute
        self.marks = marks

    def welcome(self):
        print("Welcome Mr.",self.name)
    

    def get_marks(self):
        print(f"You got {self.marks} out of 100 in Entry Test.")



s1 = Student("Afaq", 97)

s1.welcome()
s1.get_marks()


class eStudent:

    def __init__(self, name, marks):
        print("Adding new students in Database...")
        self.name = name
        self.marks = marks
        print("Welcome Mr.",self.name)
    
    @staticmethod
    def hey():
        print("Hi Everyone")


    def average_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum/3
        print(f"The average marks of {self.name} is {avg}")


st1 = eStudent("Afaq", [45,34,56])
st1.average_marks()
st1.hey()

# Static Methods
# They don't use self parameter. It's not at object level


# Abstraction

# Hiding the implementation details of the class

#Example

class Car():
    def __init__(self):
        self.accelerator = False
        self.brake = False
        self.clutch = False
    
    def start_car(self):
        self.clutch = True
        self.accelerator = True
        print("Car Has Started..")

car1 = Car()
car1.start_car()


# Encapsulation

# Wrapping data and functions into a single unit (object)


class Book():
    
    def __init__(self):
        self.title = "Alchemy"
        self.author = "Paulo Coelho"
        self.isBorrowed = True


book1 = Book()
pprint(vars(book1))

class Account():
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

