def check_if_message_exists(message_given, chat_list):
    if message_given in chat_list:
        return True
    return False

chat = []

command = input()
while command != "end":
    command_args = command.split()
    action = command_args[0]
    
    if action == "Chat":
        message = command_args[1]
        chat.append(message)
        
    elif action == "Delete":
        message = command_args[1]
        for _ in range(len(chat)):
            if check_if_message_exists(message, chat):
                chat.remove(message)
            else:
                break
            
    elif action == "Edit":
        message = command_args[1]
        new_message = command_args[2]
        for _ in range(len(chat)):
            if check_if_message_exists(message, chat):
                idx = chat.index(message)
                chat[idx] = new_message
            else:
                break
            
    elif action == "Pin":
        message = command_args[1]
        for _ in range(len(chat)):
            if check_if_message_exists(message, chat):
                chat.remove(message)
                chat.append(message)
            else:
                break
    
    elif action == "Spam":
        els_to_spam = []
        for i in range(1, len(command_args)):
            message = command_args[i]
            els_to_spam.append(message)
            
        chat.extend(els_to_spam)
    
    command = input()
    
for message in chat:
    print(message)