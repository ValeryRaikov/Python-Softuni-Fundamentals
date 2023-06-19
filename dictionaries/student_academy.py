students_dict = {}

n = int(input())
for _ in range(n):
    student_name = input()
    grade = float(input())
    
    if student_name not in students_dict:
        students_dict[student_name] = []
        
    students_dict[student_name].append(grade)
    
for student, grades in students_dict.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.5:
        print(f"{student} -> {avg_grade:.2f}")