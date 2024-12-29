#  1) Book Classs for Borrowing/Returning

class Book():
    def __init__(self, title, authhor):
        self.title = title
        self.author = authhor
        self.status = "Available"
    
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




#   2) Car Class with Start and Stop Methods:

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False
    

    def start(self):
        if self.is_running:
            self.is_running = True
            print(f"{self.brand},{self.model} is running...")
        else:
            print(f"{self.brand},{self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"Break Applied, {self.brand},{self.model} stopped..")
        else:
            print(f"{self.brand},{self.model} is not running.")
    

#   3) Student Class with grade attribute

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def average_grades(self, list_of_grades):
        self.list_of_grades = list_of_grades

        sum = 0
        for num in list_of_grades:
            sum += num
        avg = sum/len(list_of_grades)
        return avg


#   4) Employee Class with Raise Calculation:

class Employee():
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_raise(self):
        raise_percentage = float(input("Enter the percentage of raise"))
        self.salary += (raise_percentage/100)*self.salary
    
        print(f"The salary of {self.name} has become {self.salary:.2f} after {raise_percentage}%")
        


#   5)  Rectangle Class for Area and Perimeter:


class Rectangle():
    def __init__(self, length:float, width:float):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("The area of Rectangle =",area)
    
    def perimeter(self):
        perimeter = 2*(self.length + self.width)
        print("The perimeter of rectangle =", perimeter)



#  6) Dog Class with Behaviors:

class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        self.is_barking = True
        print(f"{self.name} is Barking")

    def sit(self):
        self.is_sitting = True
        print(f"{self.name} is sitting")



#   7) Library Class for Managing Books:


class Library():
    def __init__(self, list_of_books):
        self.books = list_of_books

    def add_books(self, new_books):
        self.books.extend(new_books)
        
        print(f"The available books are {self.books}")

    def remove_books(self, books_to_remove):
    
        self.books.remove(books_to_remove)
        print(f"The library has the following books: {self.books}")

