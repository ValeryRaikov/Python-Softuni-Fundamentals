import re

pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
phones = input()

results = re.findall(pattern, phones)
print(*results, sep=", ")