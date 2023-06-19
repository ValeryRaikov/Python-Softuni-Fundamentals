MAX_LITERS = 75

vehicles = {}

n = int(input())
for _ in range(n):
    car_args = input().split("|")
    car = car_args[0]
    mileage = int(car_args[1])
    fuel = int(car_args[2])
    
    if car not in vehicles:
        vehicles[car] = {"mileage": mileage, "fuel": fuel}
    else:
        vehicles[car]["mileage"] = mileage
        vehicles[car]["fuel"] = fuel
        
command = input()
while command != "Stop":
    command_args = command.split(" : ")
    action = command_args[0]
    car = command_args[1]
    
    if action == "Drive":
        distance = int(command_args[2])
        fuel = int(command_args[3])
        if vehicles[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            vehicles[car]["mileage"] += distance
            vehicles[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        
        if vehicles[car]["mileage"] >= 100000:
            vehicles.pop(car)
            print(f"Time to sell the {car}!")
        
    elif action == "Refuel":
        fuel = int(command_args[2])
        old_fuel = vehicles[car]["fuel"]
        vehicles[car]["fuel"] = min(MAX_LITERS, vehicles[car]["fuel"] + fuel)
        if vehicles[car]["fuel"] < 75:
            print(f"{car} refueled with {fuel} liters")
        else:
            print(f"{car} refueled with {MAX_LITERS - old_fuel} liters")
        
    else:
        kilometers = int(command_args[2])
        vehicles[car]["mileage"] -= kilometers
        if vehicles[car]["mileage"] < 10000:
            vehicles[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    
    command = input() 
    
for car, car_info in vehicles.items():
    print(f"{car} -> Mileage: {car_info['mileage']} kms, Fuel in the tank: {car_info['fuel']} lt.")