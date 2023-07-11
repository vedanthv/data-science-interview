def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# best case : O(n) worst and avg case : O(n^2)