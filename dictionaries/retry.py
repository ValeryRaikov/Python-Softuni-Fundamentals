language_by_username = {}
points_by_language = {}

while True:
    line = input()
    if line == "exam finished":
        break
    
    
    if "banned" in line:
        username = args[0]
        language_by_username[username].pop(username)
    else:
        args = line.split("-")
        username = args[0]
        language = args[1]
        points = int(args[2])
        
        if username not in language_by_username:
            language_by_username[username] = language
            points_by_language[language] = points
        else:
            if language_by_username[username] != language:
                language_by_username[username] = language
                points_by_language[language] = points
                continue
                
            if points_by_language[language] < points:
                points_by_language[language] = points
                
print("Results:")      
for name, lng in language_by_username.items():
    print(name, lng)  
    
print("Submissions:")
for lng, pts in points_by_language.items():
    print(lng, pts)