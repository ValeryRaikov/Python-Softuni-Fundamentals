def is_valid_index(index, text):
    return 0 <= index < len(text)


planned_tour = input()
command = input()
while command != "Travel":
    command_args = command.split(":")
    action = command_args[0]
    
    if action == "Add Stop":
        idx = int(command_args[1])
        string = command_args[2]
        if is_valid_index(idx, planned_tour):
            planned_tour = planned_tour[:idx] + string + planned_tour[idx:]
        
    elif action == "Remove Stop":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        if is_valid_index(start_idx, planned_tour) and is_valid_index(end_idx, planned_tour):
            planned_tour = planned_tour[:start_idx] + planned_tour[end_idx + 1:]
            
    else:
        old_str = command_args[1]
        new_str = command_args[2]
        if old_str in planned_tour:
            planned_tour = planned_tour.replace(old_str, new_str)
            
    print(planned_tour)
    
    command = input()
    
print(f"Ready for world tour! Planned stops: {planned_tour}")