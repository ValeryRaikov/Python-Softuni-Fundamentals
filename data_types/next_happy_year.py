current_year = int(input())
current_year += 1

year_as_string = str(current_year)
while len(year_as_string) != len(set(year_as_string)):
    current_year += 1
    year_as_string = str(current_year) 
    
else:
    print(current_year)