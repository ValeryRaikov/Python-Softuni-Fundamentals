sentence = input().split()

words = []
first_char_word = ""
for word in sentence:
    for el in word:
        if el.isdigit():
            first_char_word += el
            
    currend_word = chr(int(word[:len(first_char_word)])) + word[len(first_char_word):]
    first_char_word = ""
    
    words.append(currend_word)

final_words = []
for word in words:
    list_word = list(word)
    
    list_word[1], list_word[-1] = list_word[-1], list_word[1]
    
    for el in list_word:
        result = "".join(list_word)
    final_words.append(result)
    
print(*final_words)