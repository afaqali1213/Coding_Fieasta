def myFunc(fname,lname):
    print(fname+lname)


myFunc("Afaq", " Ali")


def frequencyy_count(text):
    letters = dict()
    for char in text.lower().split():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    print(letters)

