import re

pattern = r"\b(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"

links = []
while True:
    line = input()
    if not line:
        break
    
    matches = re.findall(pattern, line)
    links.extend([m[0] for m in matches])
    
print("\n".join(links))