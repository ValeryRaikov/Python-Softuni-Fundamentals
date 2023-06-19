def add_first_two(a, b):
    return a + b


def subtract_final(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())

result_first_two = add_first_two(first, second)
final_result = subtract_final(result_first_two, third)
print(final_result)