def selection_sort(a):
    for i in range(0,len(a)-1):
        min = i

        for j in range(i+1,len(a)-1):
            if a[j] < a[min]:
                min = j
        a[i] , a[min] = a[min] , a[i]

alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)

# best, worst and avg case TC is n^2