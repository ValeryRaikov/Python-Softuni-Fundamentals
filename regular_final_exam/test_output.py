import re

text = "##>123|yes|YES|!!!<##"
pattern = r"(.*)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})\<\1"
res = re.match(pattern, text)
print(res[2])

x= lambda x: x**3
print(x(2))

print(bool(""))

for i in range(10, 3, -2):
    print(i)
    
a = 5
b = a>2
if not a:
    print(a)
if b:
    print(b)
    
a = [1,2,3,4,5]
a.remove(3)
print(a)