contacts = {}

while True:
    command = input()
    contact = command.split("-")
    
    if len(command) == 1:
        n = int(command)
        break
    
    name = contact[0]
    phone = contact[1]
    
    contacts[name] = phone
    
for _ in range(n):
    name_to_find = input()
    if name_to_find in contacts:
        print(f"{name_to_find} -> {contacts[name_to_find]}")
    else:
        print(f"Contact {name_to_find} does not exist.")