vehicles_km = {}
vehicles_year = {}
vehicles_price = {}

command = input()
while command != "Stop":
    command_args = command.split(", ")
    car = command_args[0]
    kilometers = int(command_args[1])
    year = int(command_args[2])
    price = float(command_args[3])
    
    if car not in vehicles_km:
        vehicles_km[car] = []
        vehicles_year[car] = []
        vehicles_price[car] = []
        vehicles_km[car].append(kilometers)
        vehicles_year[car].append(year)
        vehicles_price[car].append(price)
        
    else:
        vehicles_km[car].append(kilometers)
        vehicles_year[car].append(year)
        vehicles_price[car].append(price)
        
    command = input()
    
for car, km in vehicles_km.items():
    print(f"Car {car} -> {km} km.")