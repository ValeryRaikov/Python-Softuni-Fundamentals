coffees = input().split()
number = int(input())

for _ in range(number):
    command_args = input().split()
    action = command_args[0]
    
    if action == "Include":
        coffee = command_args[1]
        coffees.append(coffee)
        
    elif action == "Remove":
        el_to_remove = command_args[1]
        num_to_remove = int(command_args[2])
        
        if num_to_remove < len(coffees):
            if el_to_remove == "first":
                for _ in range(num_to_remove):
                    coffees.pop(0)
            else:
                for _ in range(num_to_remove):
                    coffees.pop(-1)
            
    elif action == "Prefer":
        first_idx = int(command_args[1])
        second_idx = int(command_args[2])
        
        if 0 <= first_idx < len(coffees) and 0 <= second_idx < len(coffees):
            coffees[first_idx], coffees[second_idx] = coffees[second_idx], coffees[first_idx]
            
    elif action == "Reverse":
        coffees.reverse()
    
print("Coffees:")    
print(" ".join(coffees))