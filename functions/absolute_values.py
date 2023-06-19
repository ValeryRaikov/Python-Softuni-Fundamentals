def absolute(input_line = "Passed"):
    return input_line


input_line = [abs(float(num)) for num in input().split()]
print(absolute(input_line))