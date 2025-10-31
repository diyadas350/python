color_list1 = ["red", "green", "blue", "white", "black"]
color_list2 = ["yellow", "green", "white"]
result = [color for color in color_list1 if color not in color_list2]
print("colours from color-list not in color-list2:", result)
