#Module 2 - Intermediate Python Exercises
def countLetters(string):
    count = {}

    newString = string.replace(" ", "").lower()

    for char in newString:
        if char.isalpha():
            count[char] = count.get(char, 0) + 1

    return count

userInput = input("Enter a string: ")
result = countLetters(userInput)
print(result)