def reverseString(strin):
    if len(strin) == 0:
        return strin
    else:
        return reverseString[1:] + strin[0]

a = str(input("Enter the string to be reversed: "))
print(reverse(a))