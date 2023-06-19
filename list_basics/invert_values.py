input_line = input()

number_list = input_line.split()
resultant_list = []

for el in number_list:
    resultant_list.append(-int(el))
    
print(resultant_list)

##########################

this_list = [-int(num) for num in input_line.split()]
print(this_list)