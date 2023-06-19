message = input()

command = input()
while command != "Decode":
    command_args = command.split("|")
    
    action = command_args[0]
    if action == "Move":
        idx_number = int(command_args[1])
        message = message[idx_number:] + message[:idx_number]
    elif action == "Insert":
        idx = int(command_args[1])
        value = command_args[2]
        message = message[:idx] + value + message[idx:]
    else:
        old_sub = command_args[1]
        new_sub = command_args[2]
        message = message.replace(old_sub, new_sub)
    
    command = input()
    
print(f"The decrypted message is: {message}")