parking = {}

n = int(input())
for _ in range(n):
    line = input().split()
    action = line[0]
    name = line[1]
    
    if action == "register":
        license_plate = line[2]
        if name in parking:
            print(f"ERROR: already registered with plate number {parking[name]}")
        else:
            parking[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
            
    else:
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")
        
for name, plate in parking.items():
    print(f"{name} => {plate}")    