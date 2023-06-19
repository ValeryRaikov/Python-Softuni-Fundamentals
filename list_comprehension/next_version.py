first, second, third = [int(x) for x in input().split(".")]

third += 1
if third >= 10:
    third = 0
    second += 1
    if second >= 10:
        second = 0
        first += 1
        
print(f"{first}.{second}.{third}")