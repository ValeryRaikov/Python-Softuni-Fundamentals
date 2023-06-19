groceries = input().split("!")

command = input()
while command != "Go Shopping!":
    command_args = command.split()
    action = command_args[0]
    item = command_args[1]
    
    if action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
    elif action == "Correct":
        new_item = command_args[2]
        
        if item in groceries:
            groceries[groceries.index(item)] = new_item
    elif action == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
        
    command = input()
    
result = ", ".join(groceries)
print(result)