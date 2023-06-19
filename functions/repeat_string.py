string = input()
n = int(input())

repeat_strings = lambda a, b: a * b
result = repeat_strings(string, n)
print(result)

################################

def repeat_strings(string, n):
    return string * n 

print(repeat_strings(string = input(), n = int(input())))