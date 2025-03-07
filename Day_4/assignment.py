# Theater Ticketing System
import random

class Ticket:
    def __init__(self, movie_name, price, seat_number):
        self.movie_name = movie_name
        self.price = price
        self.seat_number = seat_number

    @staticmethod
    def ticket_number(length = 4):
        x = ''
        for i in range(length):
            x += str(random.randint(0,9))
        return(f"The Ticket Number is: {x}")
        

t1 = Ticket("Pushpa 2",500,"35B")

print(t1.ticket_number())


# Car Dealership Inventory

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @staticmethod
    def discounted_price(self, discount_percentage):
        print("Discounted Price: ",(discount_percentage/100)* self.price)  


