message = input()

command = input()
while command != "Reveal":
    command_args = command.split(":|:")
    action = command_args[0]
    if action == "InsertSpace":
        idx = int(command_args[1])
        message = message[:idx] + " " + message[idx:]
        print(message)
    elif action == "Reverse":
        substring = command_args[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message += substring
            print(message)
        else:
            print("error")
    else:
        substirng = command_args[1]
        replacement = command_args[2]
        message = message.replace(substirng, replacement)
        print(message)
    
    command = input()
    
print(f"You have a new text message: {message}")