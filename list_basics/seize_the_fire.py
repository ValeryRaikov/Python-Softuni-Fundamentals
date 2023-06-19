input_line = input().split("#")
water = int(input())

effort_percentage = 0.25

processed_cells = []
effort = 0
total_fire = 0
for el in input_line:
    fire_args = el.split(" = ")
    level = fire_args[0]
    value = int(fire_args[1])
    
    if level == "High" and (value < 81 or value > 125): 
        continue
    elif level == "Medium" and (value < 51 or value > 80): 
        continue
    elif level == "Low" and (value < 1 or value > 50): 
        continue
    
    if value > water:
        continue
    
    water -= value
    total_fire += value 
    effort += value * effort_percentage
    
    processed_cells.append(value)
    
print("Cells:")
for cell in processed_cells:
    print(f" - {cell}")
    
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")