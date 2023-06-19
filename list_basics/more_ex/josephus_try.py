numbers_position = input().split()
step = int(input())

extended_numbers = numbers_position * 10
k = step

excluded_people = []
for i in range(1, len(numbers_position) + 1):
    excluded_people.append(extended_numbers[step - 1])
    
    if len(excluded_people) == len(numbers_position):
        break
    
    step += k
    
print(excluded_people)