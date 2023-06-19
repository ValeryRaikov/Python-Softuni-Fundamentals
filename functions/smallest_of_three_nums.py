def find_smallest_num(numbers):
    return min(numbers)


first = int(input())
second = int(input())
third = int(input())

nums = [first, second, third]
print(find_smallest_num(nums))

################################

def find_smallest_num(numbers):
    min_num = float("inf")
    for num in nums:
        if num < min_num:
            min_num = num
            
    return min_num


first = int(input())
second = int(input())
third = int(input())

nums = [first, second, third]
print(find_smallest_num(nums))