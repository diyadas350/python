numbers=input("enter a list of integers separated by spaces: ");
numbers_list = [int(num) for num in numbers.split()]
result = []
for num in numbers_list:
    if num > 100:
        result.append('over')
    else:
        result.append(num)
print("modified list:", result)
