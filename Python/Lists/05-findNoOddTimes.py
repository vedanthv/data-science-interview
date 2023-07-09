def find_odd_occurring(alist):
    ans = 0
 
    for element in alist:
        ans ^= element
 
    return ans
 
 
alist = input('Enter the list: ').split()
alist = [int(i) for i in alist]
ans = find_odd_occurring(alist)