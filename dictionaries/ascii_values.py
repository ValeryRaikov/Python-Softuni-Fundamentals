chars = input().split(", ")
dict_comp = {char: ord(char) for char in chars}
print(dict_comp)