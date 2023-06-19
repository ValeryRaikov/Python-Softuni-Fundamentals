input_line = input().split()

command = input()
while command != "No Money":
    command_args = command.split()
    command_line =  command_args[0] 
    gift = command_args[1]
    
    if command_line == "OutOfStock":
        for i in range(len(input_line)):
            present = input_line[i]
            
            if gift == present:
                input_line[i] = "None"
            
    elif command_line == "Required":
        gift_index = int(command_args[2])
        
        if gift_index >= 0 and gift_index < len(input_line):
            input_line[gift_index] = gift
    else:
        input_line[-1] = gift
    
    command = input()
    
for gift in input_line:
    if gift == "None":
        continue
    print(gift, end = " ")
    
