#Module 2 - Intermediate Python Exercises
def getUniqueList(list):
    uniqueList = []
    for item in list:
        if item not in uniqueList:
            uniqueList.append(item)
    return uniqueList

myList = [1, 2, 3, 2, 1, 4]
uniqueList = getUniqueList(myList)
print(uniqueList)