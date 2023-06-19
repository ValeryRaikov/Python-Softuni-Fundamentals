special_word = input()
text = input()

while special_word in text:
    text = text.replace(special_word, "")
    
print(text)