# File Handling in Python

f = open("demo.txt",'r')
x = 19
# print(f.read(x))
print(f.readline())
print(f.readline())

for i in f:
    print(i)

f = open("demo.txt",'a')
f.write("Now the file has more content!")
f.close()
# f.close()
# k = open("text.txt")
# print(k)
#print(f.read())

# def frequency_count(text):
#     letters = dict()
#     for char in text.lower():
#         if char in letters:
#             letters[char] += 1
#         else:
#             letters[char] = 1
#     print(letters)

# frequency_count()


newFile = open("New_file.txt",'w')
newFile.write("""1. File Line Reader: Write a program that reads the first n lines of a file, where n is provided by the user. Print the lines to the console.

2. Word Frequency Counter: Develop a program that reads a text file and counts the frequency of each word. Display the top 5 most frequently occurring words.

3. File Character Counter: Create a program that reads a file and counts the total number of characters, excluding spaces. Print the character count to the console.

4. Append to File: Write a program that appends user-provided text to an existing file. After appending, display the updated content of the file.

5. Find Longest Word in File: Create a program that reads a text file and finds the longest word in the file. Display the word and its length.

6. Write User Input to File: Develop a program that allows the user to enter multiple lines of text and writes these lines to a new file.

7. Copy Odd Lines to Another File: Write a program that reads a file and writes only the odd-numbered lines to a new file. For example, lines 1, 3, 5, etc., should be copied.

8. File Words Beginning with a Specific Letter: Create a program that reads a file and lists all the words starting with a specific letter, entered by the user.

---""")

newFile.close()