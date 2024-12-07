shopping_list = list()

while True:
   x = int(input("""\bWelcome to the Shopping List\b
         Select the function you want to perform:
         1) Add New Item
         2) Delete any Item
         3) View Item List
         4) Exit
                   
         Enter your Selection: """))
   

   if x == 1:
       item_name = input("Enter name of item: ").upper()
       
       shopping_list.append(item_name)

   elif x ==2:
       item_name = input("Enter the item name you want to delete: ").upper()
       shopping_list.remove(item_name)
       print("Here's list after removing item", shopping_list)

   elif x ==3:
       print("The Shopping list is",shopping_list)

   elif x == 4:
       print("Thanks!")
       break
   