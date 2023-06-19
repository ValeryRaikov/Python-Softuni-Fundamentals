def check_type(input_type, operator):
    if input_type == "int":
        output = int(operator) * 2
    elif input_type == "real":
        output = f"{(int(operator) * 1.5):.2f}"
    elif input_type == "string":
        output = f"${operator}$"
    else:
        return 
        
    return output

print(check_type(input_type = input(), operator = input()))