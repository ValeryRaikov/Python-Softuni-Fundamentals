messages = {}

capacity = int(input())

line = input()
while line != "Statistics":
    line_args = line.split("=")
    action = line_args[0]
    if action == "Add":
        username = line_args[1]
        sent = int(line_args[2])
        received = int(line_args[3])
        
        if username not in messages:
            messages[username] = {"sent": sent, "received": received}
    elif action == "Message":
        sender = line_args[1]
        receiver = line_args[2]
        
        if sender in messages and receiver in messages:
            messages[sender]["sent"] += 1
            messages[receiver]["received"] += 1
            if messages[sender]["sent"] + messages[sender]["received"] >= capacity:
                print(f"{sender} reached the capacity!")
                messages.pop(sender)
            if messages[receiver]["sent"] + messages[receiver]["received"] >= capacity:
                print(f"{receiver} reached the capacity!")
                messages.pop(receiver)
    else:
        username = line_args[1]
        if username in messages:
            messages.pop(username)
        elif username == "All":
            messages.clear()
    
    line = input()
    
print(f"Users count: {len(messages)}")
for username in messages:
    print(f"{username} - {messages[username]['sent'] + messages[username]['received']}")