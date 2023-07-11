def insertionSort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i - 1
        while(j >= 0 and temp < a[j]):
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = temp

alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)


# the insertion sort algorithm encompasses a time complexity of O(n2)

# best-case time complexity of insertion sort algorithm is O(n)