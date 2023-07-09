def is_perfect_square(num):
    if num < 0:
        return False
    if num == 0:
        return True
    
    low = 1
    high = num // 2

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        
        if square == num:
            return True
        elif square < num:
            low = mid + 1
        else:
            high = mid - 1

    return False


# Example usage
num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
