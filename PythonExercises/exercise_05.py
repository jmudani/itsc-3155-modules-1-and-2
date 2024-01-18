list1 = [int(input("Enter a number for the first list: ")) for i in range(5)]
list2 = [int(input("Enter a number for the second list: ")) for i in range(5)] #Used "for _ in range" off of internet (w3schools)

def findCommonValues(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    commonValues = list(set1.intersection(set2)) #Used intersection method off of internet (w3 schools)
    return commonValues

print("First List:", list1)
print("Second List:", list2)
print("Common List:", findCommonValues(list1, list2))