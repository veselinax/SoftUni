x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

#Точка {x, y} лежи върху някоя от страните на правоъгълник {x1, y1} – {x2, y2}, ако е изпълнено едно от следните условия
first_condition =  (x == x1 or x == x2) and (y1 <= y <= y2)
second_condition = (y == y1 or y == y2) and (x1 <= x <= x2)
if first_condition or second_condition:
    print("Border")
else:
    print("Inside / Outside")

