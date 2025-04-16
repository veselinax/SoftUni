n1 = int(input())
n2 = int(input())
n3 = int(input())
max_num = 0

if n1 > n2 and n1 > n3:
    max_num = n1
elif n2 > n1 and n2 > n3:
    max_num = n2
else:
    max_num = n3
print(max_num)