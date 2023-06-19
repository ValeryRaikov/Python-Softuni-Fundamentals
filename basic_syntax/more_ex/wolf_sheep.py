queue = input()

queue_list = queue.split(", ")

if queue_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
elif queue_list[0] == "wolf":
    print(f"Oi! Sheep number {len(queue_list) - 1}! You are about to be eaten by a wolf!")
else:
    for i in range(1, len(queue_list) + 1):
        if queue_list[i] == "wolf":
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
            break