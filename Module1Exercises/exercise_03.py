userInteger = int(input("Enter an integer greater than 1: "))

def cubes(n):
    for i in range(n + 1):
        cube = i ** 3
        print(f"The cube of {i} is {cube}")

cubes(userInteger)