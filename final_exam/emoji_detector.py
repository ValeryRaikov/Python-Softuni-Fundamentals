import re

text = input()

pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

matches = re.findall(pattern, text)
total_emojis = len(matches)

treshhold = 1
for char in text:
    if char.isdigit():
        treshhold *= int(char)
        
print(f"Cool threshold: {treshhold}")
print(f"{total_emojis} emojis found in the text. The cool ones are:")

coolness = 0
for match in matches:
    symbols = match[0]
    word = match[1]
    for char in word:
        coolness += ord(char)
    if coolness > treshhold:
        print(f"{symbols}{word}{symbols}")
    coolness = 0