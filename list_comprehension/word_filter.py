input_line = input().split()

even_len_els = [el for el in input_line if len(el) % 2 == 0]

for el in even_len_els:
    print(el)