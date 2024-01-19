#Module 2 - Intermediate Python Exercises
def getCombinedDict(dict1, dict2):
    combinedDict = {}
    commonKeys = set(dict1.keys()) & set(dict2.keys())

    for key in commonKeys:
        combinedDict[key] = dict1[key] + dict2[key]

    return combinedDict

myDict1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
myDict2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combinedDict = getCombinedDict(myDict1, myDict2)
print(combinedDict)