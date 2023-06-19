def calculate(operation, num_1, num_2):
    if operation == "multiply":
        result = num_1 * num_2
    elif operation == "divide":
        result = num_1 // num_2
    elif operation == "add":
        result = num_1 + num_2
    elif operation == "subtract":
        result = num_1 - num_2
        
    return result


operation = input()
num_1 = int(input())
num_2 = int(input())

print(calculate(operation, num_1, num_2))