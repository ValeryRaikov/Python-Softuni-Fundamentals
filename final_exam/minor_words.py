import re

text = input()

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

matches = re.findall(pattern, text)

this_dict = []
for match in matches:
    first_word = match[1]
    second_word = match[2]
    
    if first_word == second_word[::-1]:
        this_dict.append(first_word)
        
if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
    
result = []
if this_dict:
    print("The mirror words are:")
    for el in this_dict:
        result.append(f"{el} <=> {el[::-1]}")
else:
    print("No mirror words!")
    
print(", ".join(result))