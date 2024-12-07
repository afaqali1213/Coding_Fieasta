contact_list = dict()

while True:
   x = int(input("""\bWelcome to the Contact Book\b
         Select the function you want to perform:
         1) Add New Contact
         2) Delete any Contact
         3) View Contact List
         4) Exit
                   
          Enter your Selection: """))
   

   if x == 1:
       name = input("Enter name of contact: ").title()
       contact = input("Enter the contact number: ")
       contact_list[name] = contact
       print(f"The contact {name} has been Added")

   elif x ==2:
       name = input("Enter the contact name you want to delete: ").title()
       contact_list.pop(name)
       print(f"The contact {name} has been deleted")

   elif x ==3:
       print(contact_list)

   elif x == 4:
       print("Thanks for using it")
       break
