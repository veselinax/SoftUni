from math import pi

figure = input()
if figure == "circle":
    radius = float(input())
    area = pi * radius * radius
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = (a * h) / 2
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "square":
    a = float(input())
    area = a*a

print(f"{area:.3f}")


