numbers = [int(a) for a in input().split(", ")]

for el in numbers:
    if el == 0:
        numbers.remove(el)
        numbers.append(el)
        
print(numbers)