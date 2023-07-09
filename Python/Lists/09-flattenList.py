my_list = [[1], [2, 3], [4, 5, 6, 7]]

flatten = [num for sublist in my_list for num in sublist]
print(flatten)