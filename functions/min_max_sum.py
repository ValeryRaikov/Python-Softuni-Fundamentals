def find_min(numbers):
    return min(numbers)


def find_max(numbers):
    return max(numbers)


def find_sum_of_nums(numbers):
    return sum(numbers)

nums = [int(x) for x in input().split()]

print(f"The minimum number is {find_min(nums)}")
print(f"The maximum number is {find_max(nums)}")
print(f"The sum number is: {find_sum_of_nums(nums)}")
