def calculate_even_uneven(number):
    even_counter = 0
    odd_counter = 0
    for el in num:
        digit = int(el)
        if digit % 2 == 0:
            even_counter += digit
        else:
            odd_counter += digit
    result = even_counter, odd_counter
    return result


num = input()

print(f"Odd sum = {calculate_even_uneven(num)[1]}, Even sum = {calculate_even_uneven(num)[0]}")