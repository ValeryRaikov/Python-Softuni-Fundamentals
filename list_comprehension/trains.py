wagons = int(input())

train = [0] * wagons

command = input()
while command != "End":
    train_args = command.split()
    first = train_args[0]
    second = int(train_args[1])
    
    if first == "add":
        train[-1] += second
    elif first == "insert":
        third = int(train_args[2])
        train[second] += third
    elif first == "leave":
        third = int(train_args[2])
        train[second] -= third
    
    command = input()
    
print(train)