nums = list(range(11))

reversed_nums = list(reversed(nums))
print(reversed_nums)

print(sorted(nums, reverse=True))

word = "Hello"
new_word = word.replace(word[1], word[-1])
print(new_word)

this_list = ["abc", "def", "ghi"]
print(this_list.index("abc"))
this_list[0], this_list[-1] = this_list[-1], this_list[0]
print(this_list)

print(word[:2])

j = 1
for i in range(1, 10):
    print(f"{i * str(j)}")
    j += 1