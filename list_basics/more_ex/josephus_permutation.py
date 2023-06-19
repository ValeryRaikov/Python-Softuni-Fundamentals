numbers_position = input().split()
step = int(input())

excluded_people = []
for i in range(1, len(numbers_position) + 1):
    excluded_people.append(numbers_position[step - 1])
    numbers_position.remove(numbers_position[step - 1])
    
    
    
print(excluded_people)