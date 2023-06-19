sentence = input()
this_dict = {}

for char in sentence:
    if char == " ":
        continue
    
    if char not in this_dict:
        this_dict[char] = 1
    else:
        this_dict[char] += 1
        
for char, occ in this_dict.items():
    print(f"{char} -> {occ}")