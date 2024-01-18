allNumbers = []
evenNumbers = []

while True:
    userInput = input("Enter a number or QUIT to quit: ")

    if userInput.upper() == "QUIT":  #Used upper method off of internet (w3 schools)
        break

    else:
        number = int(userInput)
        allNumbers.append(number)
        if number % 2 == 0:
            evenNumbers.append(number)

print("All Nums:", allNumbers)
print("Even Nums:", evenNumbers)