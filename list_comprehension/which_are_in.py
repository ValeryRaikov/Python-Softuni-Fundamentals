substrings = input().split(", ")
strings = input().split(", ")

result = []

for subword in substrings:
    for word in strings:
        if subword in word:
            result.append(subword)
            break
            
print(result)