sequence = [0, 1]

num = int(input("Enter number to which you want squence: "))
for i in range(2, num):
    next_value = sequence[i-1]+ sequence[i-2]
    sequence.append(next_value)

print("Fibonacci Sequence: ",sequence)
