n = int(input())

all_nums = []
for _ in range(n):
    num = int(input())
    
    all_nums.append(num)
    
command = input()

new_list = []
for number in all_nums:
    if command == "even":
        if number % 2 == 0:
            new_list.append(number)
    elif command == "odd":
        if number % 2 != 0:
            new_list.append(number)
    elif command == "positive":
        if number >= 0:
            new_list.append(number)
    elif command == "negative":
        if number < 0:
            new_list.append(number)
        
print(new_list)