n = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        p1 +=1
    if num % 3 == 0:
        p2 +=1
    if num % 4 == 0:
        p3 +=1
p1_perc = p1/n*100
print(f"{p1_perc:.2f}%")
p2_perc = p2/n*100
print(f"{p2_perc:.2f}%")
p3_perc = p3/n*100
print(f"{p3_perc:.2f}%")