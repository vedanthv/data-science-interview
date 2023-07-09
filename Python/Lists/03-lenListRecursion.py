def list_length(lst):
    if not lst:  # Base case: an empty list
        return 0
    else:
        return 1 + list_length(lst[1:])  # Recursive call with the remaining sublist

# Example usage
my_list = [1, 2, 3, 4, 5]
length = list_length(my_list)
print(length)  # Output: 5
