food = float(input())
hay = float(input())
cover = float(input())
guinea_weight = float(input())

food_gr = food * 1000
hay_gr = hay * 1000
cover_gr = cover * 1000
guinea_weight_gr = guinea_weight * 1000
isOk = True
for day in range(1, 31):
    if food_gr <= 0 or hay_gr <= 0 or cover <= 0:
        isOk = False
        print("Merry must go to the pet store!")
        break
    
    food_gr -= 300
    
    if day % 2 == 0:
        hay_gr -= food_gr * 0.05
        
    if day % 3 == 0:
        cover_gr -= (1 / 3) * guinea_weight_gr

if isOk:
    print(f"Everything is fine! Puppy is happy! Food: {(food_gr / 1000):.2f}, Hay: {(hay_gr / 1000):.2f}, Cover: {(cover_gr / 1000):.2f}.")