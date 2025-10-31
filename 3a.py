numbers =input("enter a list of intergers separated by spaces:")
numbers_list = [int(num) for num in numbers.split()]
positive_list = [num for num in numbers_list if num > 0]
print("postive numbers list:",positive_list)
