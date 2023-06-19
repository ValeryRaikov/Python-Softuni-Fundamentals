from string import ascii_lowercase

strings = input().split()
total_sum = 0
for substr in strings:
    first_letter = substr[0]
    last_letter = substr[-1]
    number = int(substr[1:-1])
    
    first_letter_alphabet_pos = ascii_lowercase.index(first_letter.lower()) + 1
    last_letter_alphabet_pos = ascii_lowercase.index(last_letter.lower()) + 1
    
    if first_letter.isupper():
        number /= first_letter_alphabet_pos
    else:
        number *= first_letter_alphabet_pos
    
    if last_letter.isupper():
        number -= last_letter_alphabet_pos
    else:
        number += last_letter_alphabet_pos
        
    total_sum += number
    
print(f"{total_sum:.2f}")