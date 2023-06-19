courses_dict = {}

command = input()
while command != "end":
    course_name, student_name = command.split(" : ")
    
    if course_name not in courses_dict:
        courses_dict[course_name] = []
        
    courses_dict[course_name].append(student_name)
    
    command = input()
    
for course_name, students in courses_dict.items():
    print(f"{course_name}: {len(students)}")
    
    for student_name in courses_dict[course_name]:
        print(f"-- {student_name}")