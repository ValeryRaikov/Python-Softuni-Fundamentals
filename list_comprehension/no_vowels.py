forbidden_chars = ["a", "o", "u", "e", "i"]

word = input()
new_word = [char for char in word if char.lower() not in forbidden_chars]

print(*new_word, sep="")