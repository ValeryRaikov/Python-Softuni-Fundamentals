waiting_people = int(input())
lift = [int(x) for x in input().split()]

max_people_wagon = 4

has_queue = True

for i in range(len(lift)):
    num = lift[i]
    if num <= 4:
        waiting_people -= max_people_wagon - num
        if waiting_people > 0:
            lift[i] = max_people_wagon
        else:
            lift[i] = max_people_wagon + waiting_people
        
    if waiting_people < 0:
        has_queue = False
        print("The lift has empty spots!")
        for item in lift:
            print(item, end = " ")
        break
    
if has_queue:    
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    for item in lift:
        print(item, end = " ")