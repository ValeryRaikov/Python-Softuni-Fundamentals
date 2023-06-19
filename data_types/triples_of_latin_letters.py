start = ord("a")
n = int(input())

for first in range(0, n):
    for second in range(0, n):
        for third in range(0, n):
            print(f"{chr(start + first)}{chr(start + second)}{chr(start + third)}")