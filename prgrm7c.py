list1 = list(map(int, input("enter the first list of integers(separated by spaces): ").split()))
list2 = list(map(int, input("enter the second list of integers(separated by spaces): ").split()))
common_values = set(list1) & set(list2)
if common_values:
    print("common values found:", common_values)
else:
    print("no common values found")
