from math import ceil

people = int(input())
capacity = int(input())

total_courses = ceil(people / capacity)
print(total_courses)