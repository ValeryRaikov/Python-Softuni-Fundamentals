health = 100
bitcoins = 0

MAX_HEALTH = 100

dungeons_rooms = input().split("|")

for room, el in enumerate(dungeons_rooms, start=1):
    command, number = el.split()
    number = int(number)
    
    if command == "potion":
        if health + number >= MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health =  MAX_HEALTH
        else:
            print(f"You healed for {number} hp.")
            health += number

        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        if health > number:
            health -= number
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            exit(0)
            
print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")