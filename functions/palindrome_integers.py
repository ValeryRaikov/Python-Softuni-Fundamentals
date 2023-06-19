def check_if_palindrome(numbers):
    output_line = []
    for el in numbers:
        output_line.append(el == el[::-1])
       
    return output_line
        

nums = input().split(", ")

for bool in check_if_palindrome(nums):
    print(bool)