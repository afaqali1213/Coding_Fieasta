

while True:
  word = input("Enter the word: ").lower()

  reversal = word[::-1]
  if word == reversal:
      print("It's palindrome.")
      break
  else:
      print("It's not a palindrome, Try Again")
