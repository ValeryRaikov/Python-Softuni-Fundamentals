energy = int(input())

command = input()
counter_battles = 0
has_energy = True
while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        counter_battles += 1
        energy -= distance
    else:
        has_energy = False
        print(f"Not enough energy! Game ends with {counter_battles} won battles and {energy} energy")
        break
        
    if counter_battles % 3 == 0:
        energy += counter_battles
    
    command = input()
  
if has_energy:  
    print(f"Won battles: {counter_battles}. Energy left: {energy}" )