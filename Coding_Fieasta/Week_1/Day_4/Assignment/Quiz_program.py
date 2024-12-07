answers = ['a', 'b', 'a', 'c', 'c']

print("""Answer the following Questions
      1) Who is the national poet of Pakistan?

      a) Allama Iqbal 
      b) Quaid-e-Azam
      c) Mirza Ghalib
      d) John Elia
      
      2) Who is prime minister of Pakistan?
      
      a) Imran Khan
      b) Shehbaz Sharif
      c) Nawaz Sharif
      d) None of these
      
      3) How many months are there in a year?
      
      a) 12
      b) 13
      c) 14
      d) 16
      
      4) How many Alphabets are there in English language?
      
      a) 13
      b) 25
      c) 26
      d) 37
      
      5) How many seconds are there in ah hour?
      
      a) 3440
      b) 3560
      c) 3600
      d) 3599""")

answer_1 = input("Enter the correct option for Question 1: ").lower()
answer_2 = input("Enter the correct option for Question 2: ").lower()
answer_3 = input("Enter the correct option for Question 3: ").lower()
answer_4 = input("Enter the correct option for Question 4: ").lower()
answer_5 = input("Enter the correct option for Question 5: ").lower()

score = 0
if answer_1 == answers[0]:
    score += 1
    print("Correct Answer")
else:
    print("Wrong Answer!")

if answer_2 == answers[1]:
    score += 1
    print("Correct Answer")
else:
    print("Wrong Answer!")

if answer_3 == answers[2]:
    score += 1
    print("Correct Answer")
else:
    print("Wrong Answer!")

if answer_4 == answers[3]:
    score += 1
    print("Correct Answer")
else:
    print("Wrong Answer!")

if answer_4 == answers[3]:
    score += 1
    print("Correct Answer")
else:
    print("Wrong Answer!")

print("Your Total Score is: ",score)
