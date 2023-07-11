def kth_largest_element(k):  
    global arr  
  
    # Sorts the function in reverse order  
    arr.sort(reverse = True)  
  
    # Returns the correct value  
    return arr[k-1]  
  
k = 5  
print(f"The {k}th largest element = {kth_largest_element(k)}")  