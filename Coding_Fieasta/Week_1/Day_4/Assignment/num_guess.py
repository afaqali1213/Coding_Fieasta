import random
n = int(input("Upto which number you want to guess: "))
x = random.randint(1,n)
my_set = set()
while True:
   num = int(input("Guess the number: "))
   
   if num in my_set:
       print("You Already guessed that number. Try Again!")

   my_set.add(num)
   

   if num == x:
       print("You Guessed it Right.")
       break

   elif num > x:
       print("Too High")

   elif num < x:
       print("Too Low")


print("Set of Guessed Numbers",my_set)

