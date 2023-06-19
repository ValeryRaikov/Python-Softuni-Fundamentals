submissions = {}

while True:
    line = input()
    if line == "exam finished":
        break
    
    count = 0
    if "banned" in line:
        args = line.split("-")
        username = args[0]
        del submissions[username]
        count += 1
    else:
        args = line.split("-")
        username = args[0]
        language = args[1]
        points = int(args[2])
        
        points_list = []
        
        if username not in submissions:
            points_list.append(points)
            submissions[username] = {language: points_list}
        else:
            submissions[username][language].append(points)
            
print("Results:")
for name in submissions:
    print(name, end=" ")    
    for result in submissions[name].values():
        print(f"| {max(result)}")    

print("Submissions:")
for language, subs in submissions[name]:
    print(f"{language} - {subs + count}")