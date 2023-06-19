numbers = input().split(", ")

even_index = [int(index) for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]
print(even_index)