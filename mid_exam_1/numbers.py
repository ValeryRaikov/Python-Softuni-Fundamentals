numbers = [int(x) for x in input().split()]

avg_value = sum(numbers) / len(numbers)

greatest_nums = []
counter = 0
while counter < 5:
    if max(numbers) > avg_value:
        greatest_nums.append(max(numbers))
        numbers.remove(max(numbers))
        
    counter += 1
    
if greatest_nums:
    sorted_nums = sorted(greatest_nums, reverse = True)
    for el in sorted_nums:
        print(el, end=" ")
else:
    print("No")