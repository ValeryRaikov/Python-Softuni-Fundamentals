first, second = input().split()
min_len = min(len(first), len(second))
result = 0
for i in range(min_len):
    result += ord(first[i]) * ord(second[i])
    
for i in range(min_len, len(first)):
    result += ord(first[i])
    
for i in range(min_len, len(second)):
    result += ord(second[i])
    
print(result)