text = input("enter a string:")
if len(text) > 1:
    new_string = text[-1] + text[1:-1] + text[0]
else:
    new_string = text
print("string after swapping first and last characters:", new_string)
