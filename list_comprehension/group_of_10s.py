from math import ceil

numbers = [int(x) for x in input().split(", ")]

start_boundary = 1
end_boundary = 10

final_group = ceil(max(numbers) / 10)
for i in range(1, final_group + 1):
    group_members = [x for x in numbers if start_boundary <= x <= end_boundary]
    print(f"Group of {i * 10}'s: {group_members}")
    
    start_boundary += 10
    end_boundary += 10