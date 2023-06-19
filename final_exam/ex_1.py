import re

text = input()
pattern = r"(^|\s)([\w\-]{3,16})\b"
matches = re.findall(pattern, text)


for match in matches:
    valid_name = match[1]
    print(valid_name)