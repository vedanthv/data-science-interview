n = int(input("Enter a number: "))
 
if n % 2 == 0:
    print(n, "is an even number.")
else:
    print(n, "is an odd number.")



n = int(input("Enter a number: "))
 
if n & 1:
    print(n, "is an odd number.")
else:
    print(n, "is an even number.")
