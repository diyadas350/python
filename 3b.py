n = int(input("enter how many numbers: "))
squares = []
for i in range(n):
     num = int(input(f"enter number {i+1}: "))
     squares.append(num** 2)
print("squares of the numbers are:", squares)
