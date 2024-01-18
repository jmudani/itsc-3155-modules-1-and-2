rowNum = int(input("Enter a row num from 1 to 5: "))
colNum = int(input("Enter a col num from 1 to 5: "))

for i in range(1, 6):
    for j in range(1, 6):
        if i == rowNum and j == colNum:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()