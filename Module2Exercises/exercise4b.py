#Module 2 - Intermediate Python Exercises
def inputValidation(prompt):
    while True:
        try:
            userInput = int(input(prompt))
            return userInput
        except ValueError:
            print("Invalid input. Please enter an int.")

sumResult = 0
for i in range(5):
    userValue = inputValidation(f"Enter int #{i + 1}: ")
    sumResult += userValue

print("Your sum is", sumResult)