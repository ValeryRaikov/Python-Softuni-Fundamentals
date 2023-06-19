cities = {}

command = input()
while command != "Stop":
    command_args = command.split("|")
    city_name = command_args[1]
    
    if command_args[0] == "Add":
        population = int(command_args[2])
        money_income = float(command_args[3])
        
        if city_name not in cities:
            cities[city_name] = {"Population": population, "Money income": money_income}
        else:
            cities[city_name]["Population"] += population
            cities[city_name]["Money income"] += money_income
        
    elif command_args[0] == "Update":
        object, action = command_args[2].split("<->")
        
        if city_name in cities:
            if object == "People": 
                if action == "+":
                    cities[city_name]["Population"] += int(input("Enter how many people you want to add! "))
                else:
                    cities[city_name]["Population"] -= int(input("Enter how many people you want to subtract! "))
            elif object == "Money":
                if action == "+":
                    cities[city_name]["Money income"] += int(input("Enter how much money you want to add! "))
                else:
                    cities[city_name]["Money income"] -= int(input("Enter how much money you want to subtract! "))
            else:
                print("Wrong user input!")
                continue
        else:
            print("City not found!")
            continue
        
    elif command_args[0] == "Prosper":
        if city_name in cities:
            prosperity = float(command_args[2])
            cities[city_name]["Money income"] *= (1 + prosperity)
        else:
            print("City not found!")
            continue
        
    elif command_args[0] == "Delete":
        if city_name in cities:
            del cities[city_name]
        else:
            print("City not found!")
            continue
    else:
        print("Wrong user input!")
        continue
    
    command = input()
    
print("This is your country:")
for city, city_info in cities.items():
    print(f"City: {city} -> Population: {city_info['Population']}, Money income: {city_info['Money income']}")
    
"""
example input:

Add|Tortuga|50000|110000
Add|Belmonte|30000|82550.5
Add|San Val|75000|190000
Add|Clandestina|65000|130000
Update|Tortuga|People<->+ 
Enter how many people you want to add! 5000
Update|Clandestina|Money<->-
Enter how much money you want to subtract! 10000
Prosper|San Val|0.08
Prosper|Clandestina|0.1
Delete|Belmonte
Stop
"""  