input_line = input().split()
numbers = [int(x) for x in input_line]
n = int(input())

min_num = float('inf')
for _ in range(n):
    min_num = min(numbers)
    numbers.remove(min_num)
    
for i in range(len(numbers)):
    num = numbers[i]
    if i == len(numbers) - 1:
        print(num)
    else:
        print(num, end = ", ")