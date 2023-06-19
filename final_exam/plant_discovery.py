plants_rarity = {}
plants_rating = {}

n = int(input())

for _ in range(n):
    command = input()
    plant = command.split("<->")[0]
    rarity = command.split("<->")[1]
    
    plants_rarity[plant] = rarity
    
line = input()
while line != "Exhibition":
    action = line.split(": ")[0]
    line_args = line.split(": ")[1]
    if action == "Rate":
        plant, rating = line_args.split(" - ")
        rating = float(rating)

        if plant not in plants_rating:
            plants_rating[plant] = []
            plants_rating[plant].append(rating)
        else:
            plants_rating[plant].append(rating)
            
    elif action == "Update":
        plant, new_rarity = line_args.split(" - ")
        new_rarity = int(new_rarity)
        plants_rarity[plant] = new_rarity
    else:
        plant = line.split(": ")[1]
        plants_rating[plant] = []
        
    line = input()
        
print("Plants for the exhibition:")
for plant, rarity in plants_rarity.items():
    if plants_rating[plant]:
        print(f"- {plant}; Rarity: {rarity}; Rating: {(sum(plants_rating[plant])/len(plants_rating[plant])):.2f}")
    else:
        print(f"- {plant}; Rarity: {rarity}; Rating: {0:.2f}")