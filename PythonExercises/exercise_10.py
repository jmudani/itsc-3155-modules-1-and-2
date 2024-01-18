userString = input("Enter a string: ")

charactersList = list(userString)

resultList = [charactersList[i:i+3] for i in range(0, len(charactersList), 3)]

print(resultList)