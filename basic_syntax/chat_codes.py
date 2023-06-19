total = int(input())

for _ in range(total):
    code = int(input())
    
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code != 86 and code < 88:
        print("GREAT!")
    elif code > 88:
        print("Bye.")