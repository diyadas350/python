names = input(" enter first names separated by spaces:").split()
all_names = ''.join(names)
count_a  = all_names.lower().count('a')
print("total no of occurances of 'a':", count_a)
