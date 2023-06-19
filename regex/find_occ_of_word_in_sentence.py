import re

text = input().lower()
special_word = input().lower()
pattern = rf"\b{special_word}\b"
matches = re.findall(pattern, text)

print(len(matches))