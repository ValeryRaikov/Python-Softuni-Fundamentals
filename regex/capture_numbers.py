import re

results = []
while True:
    line = input()

    if not line:
        break
    
    pattern = r"\d+"

    matches = re.findall(pattern, line)
    results.extend(matches)
    
print(*results, sep=" ")