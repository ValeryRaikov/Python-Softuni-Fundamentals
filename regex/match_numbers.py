import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
numbers = input()

results = re.finditer(pattern, numbers)
for res in results:
    print(res.group(), end=" ")