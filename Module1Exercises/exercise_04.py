n = int(input("Enter a number: "))
list = []

for i in range(n):
    value = float(input(f"Enter number {i + 1}: "))
    list.append(value) #Used append method off of internet (w3 schools)

def calculateAvg(numbers):
    return sum(numbers) / len(numbers)

average = calculateAvg(list)

print("List:", list)
print(f"Average: {average}")