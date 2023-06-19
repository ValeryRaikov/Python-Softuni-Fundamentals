from math import ceil

total_students = int(input())
number_of_lectures = int(input())
add_bonus = int(input())

max_attendances = 0
for _ in range(total_students):
    attendance = int(input())
    
    max_attendances = max(attendance, max_attendances)
        
total_bonus = 0
if number_of_lectures != 0:
    total_bonus = max_attendances / number_of_lectures * (5 + add_bonus)
    
print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")