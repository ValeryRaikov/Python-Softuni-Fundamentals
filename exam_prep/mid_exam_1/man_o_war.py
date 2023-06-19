pirateship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())

flag = True
command = input()
while command != "Retire":
    if not flag:
        break
    
    command_args = command.split()
    action = command_args[0]

    if action == "Fire":
        index = int(command_args[1])
        damage = int(command_args[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break
        
    elif action == "Defend":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        damage = int(command_args[3])
        if 0 <= start_index < len(pirateship) and 0 <= end_index < len(pirateship):
            for i in range(start_index, end_index + 1):
                pirateship[i] -= damage
                if pirateship[i] <= 0:
                    flag = False
                    print("You lost! The pirate ship has sunken.")
                    break
            
    elif action == "Repair":
        index = int(command_args[1])
        health = int(command_args[2])
        if 0 <= index < len(pirateship):
            repair = min(pirateship[index] + health, max_health)
            pirateship[index] = repair
        
    elif action == "Status":
        percentage = 0.2
        counter = 0
        for section in pirateship:
            if section < max_health * percentage:
                counter += 1
                
        print(f"{counter} sections need repair.")
    
    command = input()
    
if flag:
    print(f"Pirate ship status: {sum(pirateship)}")
    print(f"Warship status: {sum(warship)}")