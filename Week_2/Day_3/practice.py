# CSV Module practice

import csv
import json

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# with open("people.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerows(data)

# print("CSV file has been written")


# with open("people.csv","r") as f:
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)



# employees_data =[
# {
#     "name" : "Drek",
#     "age" : 25,
#     "salary" : 30000
# },

# {

#     "name" : "Trevor",
#     "age" : 35,
#     "salary" : 60000

# },

# {

#     "name" : "Hann",
#     "age" : 28,
#     "salary" : 50000

# },

# ]

# headers = ['name', 'age', 'salary']

# with open("employees.csv",'w') as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(employees_data)

