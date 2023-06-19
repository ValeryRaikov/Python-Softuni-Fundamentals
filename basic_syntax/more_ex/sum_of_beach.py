"""word = input().lower()

formed_word = ""
counter = 0
for char in word:
    formed_word += char
    
    if formed_word in ["sand", "water", "fish", "sun"]:
        counter += 1
        formed_word = ""
        
print(counter)"""

word = input().lower()

counter = 0

if "sand" in word:
    counter += 1
    word.strip("sand")
if "water" in word:
    counter += 1
    word.strip("water")
if "fish" in word:
    counter += 1
    word.strip("fish")
if "sun" in word:
    counter += 1
    word.strip("sun")

print(counter)