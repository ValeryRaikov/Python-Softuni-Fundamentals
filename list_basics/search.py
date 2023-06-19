n = int(input())
special_word = input()

all_words = []
special_words = []
for _ in range(n):
    word = input()
    
    all_words.append(word)
    
    if special_word in word:
        special_words.append(word)
        
print(f"{all_words}\n{special_words}")