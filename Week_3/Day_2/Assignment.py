#     Library System Class:

class Book():
    def __init__(self, title, authhor):
        self.title = title
        self.author = authhor
        self.status = "Available"



class Library(Book):
    def __init__(self, list_of_books):
        self.books = list_of_books

    def add_books(self, new_books):
        self.books.extend(new_books)
        
        print(f"The available books are {self.books}")

    def remove_books(self, books_to_remove):
    
        self.books.remove(books_to_remove)
        print(f"The library has the following books: {self.books}")

    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            print(f"The book {self.title} has been borrowed")
        else:
            print("Already Borrowed")
    

    def return_book(self):

        if self.status == "Borrowed":
            self.status = "Available"
            print(f"The book {self.title} has been returned and is available to borrow")
        
        else:
            print(f"The book {self.title} is already available")


    
#   Shape Class with Sub classes

class Shape():
    def area(self):
        return("The formula of Shape_area is not determined")
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = 3.14 *(self.radius**2)
        return circle_area


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5*(self.base * self.height)
    
shape = Circle(34)
print(f"The area of Circle is {shape.area()}")


#  Animal Class Hierarchy

class Animal:
    def speak(self):
        return ("I make a sound")
    


class Dog(Animal):
    def speak():
        return ("Woof!  Woof!")
    

class Cat(Animal):
    def speak(self):
        return ("Meow! Meow!")
    

class Cow(Animal):
    def speak(self):
        return("Moo!  Moo!")


def make_animal_speak(animal):
    print(animal.speak())



#   Vehicle Class Hierarchy

class Vehicle():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        print(f"The vehicle brand is {self.brand} and speed is {self.speed}km/h")


class Car(Vehicle):
    def __init__(self):
        self.air_conditioning = True
        print("Car has air conditioning system")

class Truck(Vehicle):
    def load_capacity(self, load):
        self.load = load
        print(f"The truck has load capacity of {self.load}kg")

class Bike(Vehicle):
    pass

vehicle = Vehicle("Honda","150 km/h")
car = Car()
# truck = Truck()
# bike = Bike()

print(car)

#   Person Class and Subclasses

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def attend_class(self):
        print(f"{self.name} is attending classes.")

class Teacher(Person):
    def grade_papers(self):
        print(f"{self.name} is a teacher and attending classes.")


teacher = Teacher("Afaq", 26)
student = Student("Faizan", 13)



#  Employee Management System

class Employee():
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def work(self):
        return(f"{self.name} is working in this company.")


class Manager(Employee):
    def __init__(self, name, employee_id,team_members):
        super().__init__(name, employee_id)

        self.team_members = team_members
    
    def work(self):
        return(f"{self.name} is managing a team of {self.team_members} members.")


class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)

        self.programminng_language = programming_language

    def work(self):
        return(f"{self.name} is a developer with proficiemcy in {self.programminng_language}")


employee = Employee("Raza", 2314)
manager = Manager("Raza", 2314,34)
developer = Developer("Raza", 2314,"Pyhton")


print(employee.work())
print(manager.work())
print(developer.work())