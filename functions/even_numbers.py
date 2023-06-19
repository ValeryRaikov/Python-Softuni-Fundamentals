#Using lambda function here is better than a normal function!

numbers = [int(x) for x in input().split()]
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)

even_nums_2 = [x for x in even_nums if x % 2 == 0]
print(even_nums_2)