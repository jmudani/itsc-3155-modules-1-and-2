input1 = input("Enter a string: ")
input2 = input("Enter another string: ")

def suffix(input1, input2):
    #Used endswith method off of internet (w3 schools)
    return input1.endswith(input2) or input2.endswith(input1)

print(suffix(input1, input2))