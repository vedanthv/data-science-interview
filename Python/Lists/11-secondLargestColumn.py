def find_second_largest_in_column(matrix, column_index):
    column = [row[column_index] for row in matrix]  # Extract the column from the matrix
    unique_elements = list(set(column))  # Get the unique elements in the column
    sorted_unique_elements = sorted(unique_elements)  # Sort the unique elements in ascending order

    # Check if the column has at least two unique elements
    if len(sorted_unique_elements) >= 2:
        second_largest = sorted_unique_elements[-2]  # Get the second largest element
    else:
        second_largest = None  # If there are fewer than two unique elements, set it to None

    return second_largest
