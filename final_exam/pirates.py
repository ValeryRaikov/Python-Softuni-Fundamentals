cities = {}

line = input()
while line != "Sail":
    line_args = line.split("||")
    city = line_args[0]
    population = int(line_args[1])
    gold = int(line_args[2])
    
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    
    line = input()

line = input()
while line != "End":
    line_args = line.split("=>")
    action = line_args[0]
    city = line_args[1]
    if action == "Plunder":
        people = int(line_args[2])
        gold = int(line_args[3])
        
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        
        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            print(f"{city} has been wiped off the map!")
            cities.pop(city)
    elif action == "Prosper":
        gold = int(line_args[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    
    line = input()
    
if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    
    for city, city_info in cities.items():
        print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")