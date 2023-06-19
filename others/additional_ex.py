import random

nums = []
for i in range(int(input("Enter a number: "))):
    nums.append(random.randrange(-15, 15))
    
print(f"All numbers are: {nums}")

negative_nums = [a for a in nums if a < 0]
positive_nums = [b for b in nums if b > 0]
nulls = [c if c == 0 else "Nope" for c in nums]

if len(negative_nums) > 0:
    print(f"Negative nums are: {negative_nums}")
    
if len(positive_nums) > 0:
    print(f"Positive nums are: {positive_nums}")
    
if len(nulls) > 0:
    print(nulls)
    print(f"There are {nulls.count(0)} nulls")
    
for i in range(len(positive_nums)):
    num = positive_nums[i]
    if i == len(positive_nums) - 1 and num % 2 == 0:
        print(num)
    if num % 2 == 0:
        print(num, end ="<->")
  
print()
  
for el in negative_nums:
    if el % 3 == 0:
        negative_nums.remove(el)
    else:
        negative_nums.insert(0, "Oops")
        
print(f"New negative nums: {sorted(negative_nums)}")