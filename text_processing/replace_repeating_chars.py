word = input()
result = word[0]
for char in word:
    if char != result[-1]:
        result += char    
        
print(result)