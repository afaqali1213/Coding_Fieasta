#   Static Method

# class method:


# class Person():
#     name = "Annonymous"

#     def changename(self, name):
#         self.name = name  # New name attribute
#         Person.name = name #Change the class attribute


        
# class Account():
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def resetPassword(self):
#         #self.new_pass = new_pass
#         new_pass = input("Enter the new password: ")
#         print(f"Successfully changed password from \"{self.__acc_pass}\" to \"{new_pass}\"")

# acc1 = Account("123421", "@Afaqali213")

# print(acc1.acc_no)
# print(acc1.resetPassword())


x = 5
y = "asdsd"
try:
    z = x + y

except TypeError:
    print("Error: Int cannot be added in string data type!")


# Try   Except   Elese    Finally
# The statements under finally keyword are always executed

