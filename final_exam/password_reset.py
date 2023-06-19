password = input()
new_password = ""

command = input()
while command != "Done":
    command_args = command.split()
    action = command_args[0]
    if action == "TakeOdd":
        for i in range(len(password)):
            if i % 2 != 0:
                new_password += password[i]
        print(new_password)
    elif action == "Cut":
        index = int(command_args[1])
        length = int(command_args[2])
        substr = new_password[index: index + length]
        new_password = new_password.replace(substr, "", 1)
        print(new_password)
    else:
        substring = command_args[1]
        substitute = command_args[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")
    
    command = input()
    
print(f"Your password is: {new_password}")