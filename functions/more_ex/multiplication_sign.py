def find_sign_first(a, b):
    if first == 0 or second == 0:
        result = "zero"
    elif first < 0 and second < 0:
        result = "positive"
    elif first < 0 or second < 0:
        result = "negative"
    else:
        result = "positive"
        
    return result

def find_sign_second(a, b):
    if result_first == "zero" or third == 0:
        result = "zero"
    elif result_first == "negative" and third < 0:
        result = "positive"
    elif result_first == "negative" or second < 0:
        result = "negative"
    elif result_first == "positive" and third < 0:
        result = "negative"
    else:
        result = "positive"
        
    return result
    

first = int(input())
second = int(input())
third = int(input())

result_first = find_sign_first(first, second)
result_second = find_sign_second(first * second, third)
print(result_second)