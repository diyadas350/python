list1 = list(map(int, input("enter the first list of integers(separated by spaces): ").split()))
list2 = list(map(int, input("enter the second list of integers(separated by spaces): ").split()))
if len(list1) == len(list2):
    print("both the lists are of the same length.")
else:
    print("the lists are of different lengths.")
sum1 = sum(list1)
sum2 = sum(list2)
if sum(list1) == sum(list2):
    print("the sum of the two list are same")
else:
    print("not")
