vowels = ['a', 'e', 'i', 'o', 'u']

alphabet = input("Enter any Alphabet: ").lower()

if alphabet in vowels:
    print(f"{alphabet} is a Vowel")
else:
    print(f"{alphabet} is a Consonent")
