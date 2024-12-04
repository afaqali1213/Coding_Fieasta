password = input("Enter your Password: ")

# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# special_char = "!@#$%^&*()_-+=?/><.,`~"

# for i in password:
#     if i in upper_case and i in lower_case and i in special_char and len(password) >= 8:
#         print("It's a strong password")
# else:
#     print("Make it stronger")


for i in password:
    print(i)

if len(password) >= 8:
    print("Strong Password")
