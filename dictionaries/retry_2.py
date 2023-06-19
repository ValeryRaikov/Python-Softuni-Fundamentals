points_by_username = {}
subs_by_language = {}

while True:
    line = input()
    if line == "exam finished":
        break
    
    if "banned" in line:
        args = line.split("-")
        username = args[0]
        
        if username in points_by_username:
            del points_by_username[username]
    else:
        args = line.split("-")
        username = args[0]
        language = args[1]
        points = int(args[2])
        
        if username not in points_by_username:
            points_by_username[username] = points
        else:
            if points > points_by_username[username]:
                points_by_username[username] = points
                
        if language not in subs_by_language:
            subs_by_language[language] = 1
        else:
            subs_by_language[language] += 1  
            
print("Results:")
for name, pts in points_by_username.items():
    print(f"{name} | {pts}")
    
print("Submissions:")
for lng, subs in subs_by_language.items():
    print(f"{lng} - {subs}")