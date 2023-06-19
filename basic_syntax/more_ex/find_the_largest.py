number = int(input())

number_as_string = str(number)
number_list = []

for digit in number_as_string:
    number_list.append(digit)

number_list.sort(reverse=True)

largest_num_string = "".join(number_list)

largest_num = int(largest_num_string)
print(largest_num)