def find_between_chars(start, end):
    chars_in_range = []
    for el in range(ord(start) + 1, ord(end)):
        chars_in_range.append(chr(el))
        
    return chars_in_range


start_char = input()
end_char = input()

for el in find_between_chars(start_char, end_char):
    print(el, end = " ")