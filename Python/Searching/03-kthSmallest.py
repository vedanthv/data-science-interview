def kthSmallest(arr, N, K):
 
    # Sort the given array
    arr.sort()
 
    # Return k'th element in the
    # sorted array
    return arr[K-1]