def check_if_valid(name, this_dict):
    return name in this_dict

plants_rarity = {}
plants_rating = {}

n = int(input())

for _ in range(n):
    command = input()
    plant = command.split("<->")[0]
    rarity = command.split("<->")[1]
    
    plants_rarity[plant] = rarity
    plants_rating[plant] = []
    
line = input()
while line != "Exhibition":
    action = line.split(": ")[0]
    line_args = line.split(": ")[1]
    if action == "Rate":
        plant, rating = line_args.split(" - ")
        rating = float(rating)
        if check_if_valid(plant, plants_rating):
            plants_rating[plant].append(rating)
        else:
            print("error")
    elif action == "Update":
        plant, new_rarity = line_args.split(" - ")
        new_rarity = int(new_rarity)
        if check_if_valid(plant, plants_rarity):
            plants_rarity[plant] = new_rarity
        else:
            print("error")
    else:
        plant = line.split(": ")[1]
        if check_if_valid(plant, plants_rating):
            plants_rating[plant] = []
        else:
            print("error")
        
    line = input()
        
print("Plants for the exhibition:")
for plant, rarity in plants_rarity.items():
    if plants_rating[plant]:
        print(f"- {plant}; Rarity: {rarity}; Rating: {(sum(plants_rating[plant])/len(plants_rating[plant])):.2f}")
    else:
        print(f"- {plant}; Rarity: {rarity}; Rating: {0:.2f}")