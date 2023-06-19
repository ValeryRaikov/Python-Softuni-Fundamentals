numbers_list = [int(a) for a in input().split()]

left_car_times = [numbers_list[i] for i in range(len(numbers_list)) if i < len(numbers_list) / 2]
left_car_times.pop()
right_car_times = [numbers_list[i] for i in range(len(numbers_list)) if i > len(numbers_list) / 2]

sum_left = 0
for num_left in left_car_times:
    if num_left == 0:
        sum_left *= 0.8
    else: 
        sum_left += num_left
    
sum_right = 0
for i in range(1, len(right_car_times) + 1):
    num_right = right_car_times[-i]
    if num_right == 0:
        sum_right *= 0.8
    else: 
        sum_right += num_right
    
if sum_left < sum_right:
    print(f"The winner is left with total time: {sum_left:.1f}")
else:
    print(f"The winner is right with total time: {sum_right:.1f}")