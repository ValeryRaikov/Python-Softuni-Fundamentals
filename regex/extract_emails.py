import re

emails = input()
pattern = r"\s([A-Za-z0-9][\w\.\-]*[A-Za-z0-9]@[A-Za-z][A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)"
matches = re.findall(pattern, emails)

for groups in matches:
    print(groups[0])