text = input()
emoticon = ""
for i in range(len(text)):
    char = text[i]
    if char == ":":
        emoticon = text[i:i+2]
        print(emoticon)