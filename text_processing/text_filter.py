forbidden_words = input().split(", ")
text = input()

for word in forbidden_words:
    text = text.replace(word, "*" * len(word))
    
print(text)