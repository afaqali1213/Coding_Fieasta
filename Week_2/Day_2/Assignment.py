#                         Day 1

# 1) File Line Reader

f = open("demo.txt","r")
x = int(input("Enter number of lines you want to read from the file: "))
for i in range(1,x+1):      
    print(f.readline())

print(f.close())


# 2) Append the file with user provided text

f = open("demo.txt", 'a')
text = input("Enter the text you want to append to the file: ")

f.write(text)
f.close()


# 3) User provided text

content = input("Enter the content you want to save in new file: ")

userFile = open("user_File", "w") # 'w' writes the new content every time ou run the program.
userFile.writelines(content)
userFile.close()

userFile = open("user_File",'r')
print(userFile.read())

userFile.close()


# 4) Word Frequency Counter


f = open("E:\Coding_Fieasta\Week_2\Day_2\demo.txt","r")
content = f.read()
print(content)

lowerCase_content = content.lower().split()
word_counter = dict()

for words in lowerCase_content:
    if words in word_counter:
        word_counter[words] += 1
    else:
        word_counter[words] = 1


def sort_by_frequency(item):
    return item[1]


print("The words frequency are as follows:\n",word_counter)
sort_dictionary = sorted(word_counter.items(), key=sort_by_frequency, reverse=True)


frequent_words = sort_dictionary[:5]
print("The 5 frequent words are: ",frequent_words)

f.close()


# 5) Finding the longest word

words_length = dict()
with open(r"E:\Coding_Fieasta\Week_2\Day_2\demo.txt","r") as file:
    letters = file.read()
    words = letters.split()

for word in words:
    words_length[word] = len(word)

longest_word = max(words_length, key=words_length.get)

print(f"The longest word in the file is {longest_word}")


# 6) Words start with specific letter

letter = input("Enter a letter: ").lower()
words_list = list()
with open(r"E:\Coding_Fieasta\Week_2\Day_2\demo.txt","r") as file:
   letters = file.read()
   words = letters.split()

for word in words:
  if word[0] == letter:
      words_list.append(word)

if len(words_list) == 0:
   print(f"No word with the letter \'{letter}\' found in the file.")

print(words_list)


# 7) Character Counter in the file


with open(r"E:\Coding_Fieasta\Week_2\Day_2\demo.txt","r") as file:
   letters = file.read()
   words = letters.split()

total_characters = 0
for word in words:
   total_characters += len(word)

print(f"Total Characters in the file are {total_characters}")


# 8) Odd number of Lines

with open("E:\Coding_Fieasta\Week_2\Day_2\demo.txt",'r') as source_file, open("Odd_lines.txt", 'w') as destignated_file:
    for index, line in enumerate(source_file):
        if index%2 == 0:
            destignated_file.write(line)
            
