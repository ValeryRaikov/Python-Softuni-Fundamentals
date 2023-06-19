rooms = int(input())

free_chairs = 0
needed_chairs = 0
isOk = True
for room in range(1, rooms + 1):
    chairs, visitors = input().split()
    
    if len(chairs) >= int(visitors):
        free_chairs += len(chairs) - int(visitors)
    else:
        isOk = False
        needed_chairs += int(visitors) - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
        needed_chairs = 0
    
if isOk:
    print(f"Game On, {free_chairs} free chairs left")