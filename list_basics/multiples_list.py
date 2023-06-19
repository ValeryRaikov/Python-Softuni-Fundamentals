factor = int(input())
count = int(input())

resultant_list = []
for num in range(factor, factor * count + 1, factor):
    resultant_list.append(num)
    
print(resultant_list)

############################

factor = int(input())
count = int(input())

resultant_list = []
for num in range(1, count + 1):
    resultant_list.append(num * factor)
    
print(resultant_list)