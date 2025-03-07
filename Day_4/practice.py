# Static Methods and Class Methods

class Person:
    __name = "Annonymous"

    def __hey(self):
        print("Hey There !")

    def welcome(self):
        self.__hey()

p1 = Person()

try:
    print(p1.__hey)
except AttributeError:
    print("Can't call it's private")
print(p1.welcome())

class Car:
    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")


