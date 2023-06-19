def print_grade(grade):
    if 2 <= grade <= 2.99:
        note = "Fail"
    elif 3 <= grade <= 3.49:
        note = "Poor"
    elif 3.5 <= grade <= 4.49:
        note = "Good"
    elif 4.5 <= grade <= 5.49:
        note = "Very Good"
    elif 5.50 <= grade <= 6:
        note = "Excellent"
        
    return note


grade = float(input())
print(print_grade(grade))