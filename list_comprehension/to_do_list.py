command = input()

to_do_list = [0] * 10

while command != "End":
    command_args = command.split("-")
    importance = int(command_args[0])
    task = command_args[1]
    
    index = importance - 1
    
    to_do_list[index] = task
    
    command = input()
    
print([task for task in to_do_list if task != 0])