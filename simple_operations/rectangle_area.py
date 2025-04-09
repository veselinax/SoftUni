x1 = float(input())
y1 = float(input())
x2= float(input())
y2 = float(input())
a = abs(x2 - x1)               # (x1,y1) - (x2,y2) = x2 - x1 , y2 - y1
b = abs(y2 - y1)               # abs so we avoid negative invalid numbers for example if x2 = 10, y2 = 60 final answer is 50 not -50
area = a * b
perimeter = 2 * (a+b)
print(f"{area:.2f}")
print(f"{perimeter:.2f}")