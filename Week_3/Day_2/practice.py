#  Inherritance


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



class Library(Book):
    def __init__(self, list_of_books):
        self.books = list_of_books

    def add_books(self, new_books):
        self.books.extend(new_books)
        
        print(f"The available books are {self.books}")

    def remove_books(self, books_to_remove):
    
        self.books.remove(books_to_remove)
        print(f"The library has the following books: {self.books}")



#  Polymorphism

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


dog = Dog()
cat = Cat()
cow = Cow()

make_animal_speak(cow)


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