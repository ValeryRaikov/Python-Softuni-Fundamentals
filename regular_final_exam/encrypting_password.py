import re

pattern = r"(.*)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})\<\1"

result = re.compile(pattern)
all_passwords = []

empty_str = ""

n = int(input())
for _ in range(n):
    password = input()
    
    result = re.match(pattern, password)
    if not result:
        print("Try another password!")
    else:
        all_passwords.append(password)
        first_group = result[2]
        second_group = result[3]
        third_group = result[4]
        fourth_group = result[5]
        
        whole_group = first_group + second_group + third_group + fourth_group
        print(f"Password: {whole_group}")