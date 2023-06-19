command = input()

my_mine = {}
resources = []
quantities = []

counter = 0
while command != "stop":
    counter += 1
    
    if counter % 2 != 0:
        resource = command
        resources.append(resource)
    else:
        quantity = int(command)
        quantities.append(quantity)
        
    command = input()
    
for i in range(counter//2):
    resource = resources[i]
    quantity = quantities[i]
    if resource not in my_mine:
        my_mine[resource] = quantity
    else:
        my_mine[resource] += quantity
        
for res, qnt in my_mine.items():
    print(f"{res} -> {qnt}")
    
##########################################

my_mine = {}
while True:
    line = input()
    if line == "stop":
        break
    
    quantity = int(input())
    
    if line not in my_mine:
        my_mine[line] = quantity
    else:
        my_mine[line] += quantity
        
for res, qnt in my_mine.items():
    print(f"{res} -> {qnt}")