n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 +=1
    elif 400 <= num <= 599:
        p3 +=1
    elif 600 <= num <= 799:
        p4 += 1
    else:
        p5 += 1
p1_percentage = p1 / n*100
print(f"{p1_percentage:.2f}%")
p2_percentage = p2 / n*100
print(f"{p2_percentage:.2f}%")
p3_percentage = p3 / n*100
print(f"{p3_percentage:.2f}%")
p4_percentage = p4 / n*100
print(f"{p4_percentage:.2f}%")
p5_percentage = p5 / n*100
print(f"{p5_percentage:.2f}%")
