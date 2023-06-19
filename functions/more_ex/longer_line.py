from math import floor

def check_coordinates(x1, y1, x2, y2, x3, y3, x4, y4):
    if (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) / 2 >= (abs(x3  -x4) ** 2 + abs(y3 - y4) ** 2) / 2:
        if (abs(x1) ** 2 + abs(y1) ** 2) / 2 <= (abs(x2) ** 2 + abs(y2) ** 2) / 2:
            output = f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        else:
            output = f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    else:
        if (abs(x1) ** 2 + abs(y1) ** 2) / 2 >= (abs(x2) ** 2 + abs(y2) ** 2) / 2:
            output = f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"
        else:
            output = f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})"

    return output


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(check_coordinates(x1, y1, x2, y2, x3, y3, x4, y4))