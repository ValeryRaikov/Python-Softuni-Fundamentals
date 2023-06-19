numbers = [int(x) for x in input().split(", ")]

pos = []
neg = []
even = []
odd = []
for num in numbers:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)
        
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
        
print(f'Positive: {", ".join([str(num) for num in pos])}\nNegative: {", ".join([str(num) for num in neg])}\nEven: {", ".join([str(num) for num in even])}\nOdd: {", ".join([str(num) for num in odd])}')