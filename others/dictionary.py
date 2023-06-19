students = {
    1: {"name": "Valery Raikov",
        "id": 121222139,
        "university": "TU",
        "faculty": "FCSE"},
    2: {"name": "Philip Naydenov",
        "id": "1439EP56",
        "university": "MU",
        "faculty": "FDM"},
    3: {"name": "Ivaylo Yordanov",
        "id": 196842032,
        "university": "UNWE",
        "faculty": "FIWC"}
}

for student in students:
    for key, info in students[student].items():
        print(f"{key} -> {info}")
        
search_for_student = input("Enter student name: ")
for student in students:
    if search_for_student in students[student]["name"]:
        print("Student information:")
        for key, value in students[student].items():
            print(f"{key} -> {value}")
        break
    else:
        print(f"{search_for_student} not found!")
        break