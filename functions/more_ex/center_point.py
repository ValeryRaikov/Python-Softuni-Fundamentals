from math import floor

def check_coordinates(x1, y1, x2, y2):
    if (abs(x1) ** 2 + abs(y1) ** 2) / 2 <= (abs(x2) ** 2 + abs(y2) ** 2) / 2:
        output = f"({floor(x1)}, {floor(y1)})"
    else:
        output = f"({floor(x1)}, {floor(y1)})"

    return output


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(check_coordinates(x1, y1, x2, y2))
