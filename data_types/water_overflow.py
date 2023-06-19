capacity = 255

n = int(input())

total_liters_poured = 0
for _ in range(n):
    liters = int(input())
    
    if liters > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= liters
        total_liters_poured += liters
        
print(total_liters_poured)