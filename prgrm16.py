str1 = input("entr first number:")
str2 = input("enter second number:")
new_str1 = str2[:1] + str1[1:]
new_str2 = str1[:1] + str2[1:]
result = new_str1 + " " + new_str2
print("resulting string:", result)

