name = input()

while True:
    isTrue = True
    
    if name == "Welcome!":
        break
    if name == "Voldemort":
        print("You must not speak of that name!")
        isTrue = False
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
        
    name = input()
    
if isTrue:
    print("Welcome to Hogwarts.")