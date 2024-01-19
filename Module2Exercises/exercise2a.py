#Module 2 - More python Exercises
userInput = input("Enter a string: ")

lowercaseLetters = ''.join(char for char in userInput if char.islower())
uppercaseAndSpaces = ''.join(char for char in userInput if char.isupper()) #found methods/functions online (w2schools)

print(lowercaseLetters + uppercaseAndSpaces)
