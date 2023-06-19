code = [a for a in input().split()]
message = input()

message_list = []
for char in message:
    message_list.append(char)
    
counter = 0
char_at_index = 0
for num in code:
    for digit in num:
        counter += int(digit)
        
    if counter > len(message_list):
        char_at_index = counter - len(message_list) 
    else:
        char_at_index = counter
        
    print(message_list[char_at_index], end="")
    message_list.remove(message_list[char_at_index])
    
    counter = 0