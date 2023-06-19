import re

text = input()

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

matches = re.findall(pattern, text)

total_points = 0
for match in matches:
    destination = match[1]
    total_points += len(destination)
    
print(f"Destinations: {', '.join([m[1] for m in matches])}")
print(f"Travel Points: {total_points}")