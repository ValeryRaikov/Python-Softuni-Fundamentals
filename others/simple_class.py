class Student:
    def __init__(self, first_name, last_name, age, lectures, points):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.lectures = lectures
        self.points = points
        
    def __repr__(self):
        return f"Student {self.first_name} {self.last_name} of age {self.age} has the following {self.lectures} lectures!"
        
    def check_for_discipline(self, lecture="None"):
        if lecture in self.lectures:
            return f"{lecture} already in {self.first_name}'s lectures!"
        
        self.lectures.append(lecture)
        return f"{lecture} added to {self.first_name}'s lectures! --> {self.lectures}"
    
    def add_credits(self):
        group_A = ["Materials", "Physics", "Mechanics"]
        group_B = ["Engineering", "Architecture", "Maths"]
        group_C = ["Programming", "Biology", "Chemistry"]
        
        for lecture in self.lectures:
            if lecture in group_A:
                self.points += 10
            elif lecture in group_B:
                self.points += 15
            elif lecture in group_C:
                self.points += 20
                    
        return f"{self.first_name} has {self.points} points total."
    
    def check_if_pass(self):
        if self.points >= 50:
            return f"{self.first_name} has enough points to pass!"
        
        return f"{self.first_name} should retake the year!"
    
students = [
    Student("Valery", "Raikov", 19, ["Programming", "Maths", "Mechanics", "Materials"], 10),
    Student("Ivan", "Motovski", 17, ["Biology", "Maths", "Chemistry", "Physics"], 5),
    Student("Marta", "Zlatkova", 19, ["Engineering", "Maths", "Architecture", "Physics"], 10)
    ]

#outer method:
def sort_by_age(students):
    sorted_students = sorted(students, key=lambda x: x.age)
    for student in sorted_students:
        print(student)
        
sort_by_age(students)

#printing and displaying output!
for i in range(len(students)):
    student = students[i]
    print(student.check_for_discipline(input("Enter lecture to check: ")))
    print(student.add_credits())
    print(student.check_if_pass())