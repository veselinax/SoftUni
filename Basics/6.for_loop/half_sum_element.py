import sys

n = int(input())
sum = 0
max_number = -sys.maxsize

for i in range(n):
    num = int(input())
    if num > max_number:
        max_number = num
    sum += num
sum -= max_number
if sum == max_number:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {(abs(max_number - sum))}")
