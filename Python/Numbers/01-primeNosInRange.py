r=int(input("Enter upper limit: "))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)

# Recursion

def check(num,div = None)
    if div == None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("No not prime")
            return False
        else:
            return check(num,div - 1)

    else:
        return True