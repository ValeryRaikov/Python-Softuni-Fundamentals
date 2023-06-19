all_words = input().split()
special_word = input()

palindrome_words = [word for word in all_words if word[::-1] == word]
total_matches = palindrome_words.count(special_word)
print(palindrome_words)
print(f"Found palindrome {total_matches} times")