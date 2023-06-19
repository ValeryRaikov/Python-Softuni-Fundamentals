activation_key = input()

command = input()
while command != "Generate":
    command_args = command.split(">>>")
    action = command_args[0]
    if action == "Contains":
        substring = command_args[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        flip_to = command_args[1]
        start_idx = int(command_args[2])
        end_idx = int(command_args[3])
        if flip_to == "Upper":
            activation_key = activation_key[: start_idx] + activation_key[start_idx: end_idx].upper() + activation_key[end_idx:]
        else:
            activation_key = activation_key[: start_idx] + activation_key[start_idx: end_idx].lower() + activation_key[end_idx:]
        print(activation_key)
    else:
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        activation_key = activation_key[:start_idx] +  activation_key[end_idx:]
        print(activation_key)
    
    command = input()
    
print(f"Your activation key is: {activation_key}")