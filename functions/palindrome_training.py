num = input()
num_as_int = int(num)

reversed_num = []
for _ in num:
    last_digit = num_as_int % 10
    reversed_num.append(str(last_digit))
    
    num_as_int //= 10
    

num_as_str = "".join(reversed_num)
    
if num == num_as_str:
    print("palindrome")
else:
    print("not a palindrome")