# The intuition of the algorithm is not to consider the subarray as a part of the answer if its sum is less than 0. A subarray with a sum less than 0 will always reduce our answer and so this type of subarray cannot be a part of the subarray with maximum sum.

import sys
def maxSubarraySum(arr, n):
    maxi = -sys.maxsize-1 
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi
