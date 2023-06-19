lessons = input().split(", ")

flag = False

command = input()
while command != "course start":
    command_args = command.split(":")
    action = command_args[0]
    lessons_title = command_args[1]
    
    if action == "Add":
        if lessons_title not in lessons:
            lessons.append(lessons_title)
    elif action == "Insert":
        index = int(command_args[2])
        if lessons_title not in lessons:
            lessons.insert(index, lessons_title)
    elif action == "Remove":
        if lessons_title in lessons:
            lessons.remove(lessons_title)
        if flag:    
            lessons.remove(exercise)
            flag = False
    elif action == "Swap":
        second_lessons_title = command_args[2]
        if lessons_title in lessons and second_lessons_title in lessons:
            idx_first = lessons.index(lessons_title)
            idx_second = lessons.index(second_lessons_title)
            lessons[idx_first], lessons[idx_second] = lessons[idx_second], lessons[idx_first]
        if flag:
            lessons.remove(exercise)
            lessons.insert(idx_first + 1, exercise)
            flag = False
    if action == "Exercise":
        flag = True
        exercise = f"{lessons_title}-Exercise"
        if lessons_title in lessons:
            lessons[lessons_title] = exercise
        else:
            lessons.append(lessons_title)
            lessons.append(exercise)
    
    command = input()
    
for i in range(1, len(lessons) + 1):
    print(f"{i}.{lessons[i-1]}")