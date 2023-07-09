def find_union(list1, list2):
    union = list1.copy()  # Make a copy of the first list
    
    # Add elements from the second list to the union list
    for element in list2:
        if element not in union:
            union.append(element)
    
    return union

# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
union = find_union(list1, list2)
print(union)
