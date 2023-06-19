text = input()
result = ""
for char in text:
    char = chr(ord(char) + 3)
    result += char
    
print(result)

encrypted_text = "".join([chr(ord(char) + 3) for char in text])
print(encrypted_text)