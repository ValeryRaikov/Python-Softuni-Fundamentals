import sys

n = int(input())

highest_weight = 0
highest_time = 0
highest_quality = 0 
highest_value = -sys.maxsize
for i in range(1, n + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    
    value_per_ball = (weight / time) ** quality
    
    if value_per_ball > highest_value:
        highest_weight = weight
        highest_time = time
        highest_quality = quality 
        highest_value = value_per_ball
        
print(f"{highest_weight} : {highest_time} = {highest_value:.0f} ({highest_quality})")