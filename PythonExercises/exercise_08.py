originalList = []

for i in range(10):
    userInput = input(f"Enter number {i + 1}: ")
    originalList.append(int(userInput))
uniqueList = [element for element in originalList if originalList.count(element) == 1] 

print("Original List:", originalList)
print("Nums that appear once:", uniqueList)