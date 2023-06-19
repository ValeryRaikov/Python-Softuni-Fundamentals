number_of_words = int(input())

for _ in range(number_of_words):
    word = input()
    
    isPure = True
    for char in word:
        if char in [",", ".", "_"]:
            print(f"{word} is not pure!")
            isPure = False
            break
    if isPure:
        print(f"{word} is pure.")