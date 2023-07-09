def find_intersection(list1, list2):
    intersection = []  # Make a copy of the first list
    
    # Add elements from the second list to the union list
    for element in list1:
        if element in list2:
            intersection.append(element)
    
    return intersection

# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = find_intersection(list1, list2)
print(intersection)
