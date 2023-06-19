coffee = 0

line = input()
while True:
    if line == "END":
        break
    
    if line not in ["coding", "cat", "dog", "movie", "CODING", "CAT", "DOG", "MOVIE"]:
        line = input()
        continue
    
    if line.isupper():
        coffee += 2
    else:
        coffee += 1
        
    line = input()
        
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)