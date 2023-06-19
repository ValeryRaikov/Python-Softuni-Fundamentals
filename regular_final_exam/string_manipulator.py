text = input()

command = input()
while command != "End":
    command_args = command.split()
    action = command_args[0]
    if action == "Translate":
        char = command_args[1]
        replacement = command_args[2]
        text = text.replace(char, replacement)
        print(text)
    elif action == "Includes":
        substring = command_args[1]
        if substring in text:
            print("True")
        else:
            print("False")
    elif action == "Start":
        substring = command_args[1]
        if text.startswith(substring):
            print("True")
        else:
            print("False")
    elif action == "Lowercase": 
        text = text.lower()
        print(text)
    elif action == "FindIndex":
        char = command_args[1]
        i = text.rfind(char)
        print(i)
    else:
        start_idx = int(command_args[1])
        count = int(command_args[2])
        text = text[:start_idx] + text[start_idx + count:]
        print(text)
           
    command = input()