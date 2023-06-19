command = input()

courses = {}

while ":" in command:
    student_name, student_id, course_name = command.split(":")
    
    if course_name not in courses:
        courses[course_name] = {student_id: student_name}
    else:
        courses[course_name][student_id] = student_name
    
    command = input()
    
course_name = command.replace("_", " ")
students = courses[course_name]

for student_id, student_name in students.items():
    print(f"{student_name} - {student_id}")
