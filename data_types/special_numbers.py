n = int(input())

for num in range(1, n + 1):
    isSpecial = False
    sum_of_digits = 0
    digits = num
    
    while digits:
        sum_of_digits += digits % 10
        
        digits //= 10
        
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        isSpecial = True
        print(f"{num} -> {isSpecial}")
    else:
        print(f"{num} -> {isSpecial}")