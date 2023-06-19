current_strings = input().split()
input_line = input()
new_lst = []
while input_line != "3:1":
    command, first_index, last_index = input_line.split()
    if command == "merge":
        first_index = int(first_index)
        last_index = int(last_index)
        if first_index < 0:
            first_index = 0
        if last_index > len(current_strings) - 1:
            last_index = len(current_strings) - 1
        for el in range(len(current_strings)):
            if el in range(first_index + 1, last_index + 1):
                current_strings[first_index] += current_strings[el]
        for index in range(last_index, first_index, -1):
            current_strings.pop(index)
 
    elif command == "divide":
        index = int(first_index)
        partitions = int(last_index)
        if partitions > len(current_strings[index]):
            step = 1
        else:
            step = len(current_strings[index]) // partitions
        divide_part = current_strings.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                current_strings.insert(index, divide_part[start::])
                break
            else:
                current_strings.insert(index, divide_part[start: start + step:])
            start += step
            index += 1
    input_line = input()
print(' '.join(current_strings))