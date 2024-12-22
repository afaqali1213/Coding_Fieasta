#   Day 1


# 1) Function to calculate factorial

def factorial(number):
    product = 1
    for i in range(1,number+1):
        product *= i
    print(f"The factorial of {number} is {product}")



# 2) Function to calculate Fibonacci Sequence

def fibonacci(number):
    sequence = [0,1]
    for i in range(2,number):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)

    print(f"The fibonacci squence of {number} is {sequence}")



# 3) Function to find if given Number is even or odd

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

print(is_even(5))



# 4) Function to find squares of elements of a list


def sum_of_squares(numbers):
    squared_list = list()
    sum = 0
    for num in numbers:
        squared = num**2
        squared_list.append(squared)
        for squares in squared_list:
          sum += squares
    print(f"Sum of {squared_list} is {sum}")


sum_of_squares([1,2,3])


# 5) Function to calculate string length

def calculate_length(s):
    print(f"The length of string {s} is {len(s)}")



# 6) Function to generate Prime Numbers

def generate_primes(number):
    primes = list()
    for i in range(2,number):
        for j in range(2,i):
           if i % j == 0:
              break
        else:
           primes.append(i)
    print(primes)



generate_primes(10)

# 7) Function to convert Units

def converts_unit(value,unit_from, unit_to):
    if unit_from == "km" and unit_to == "miles":
        print(f"The {value}{unit_from} is {value * 0.621}{unit_to}")
    elif unit_from == "miles" and unit_to == "km":
        print(f"The {value}{unit_from} is {value / 0.621}{unit_to}")

converts_unit(10,"KM","MiLes")
converts_unit(6.21,"miles","km")



# 8) Letter Frequency Counter

def letter_frequency(text):
    letters = dict()
    for char in text.lower():
        if char in letters:
            letters[char] +=1
        else:
            letters[char] = 1
    print(letters)

letter_frequency("aASDA")

