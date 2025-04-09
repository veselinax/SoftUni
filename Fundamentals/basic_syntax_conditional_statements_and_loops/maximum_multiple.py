divisor = int(input())
bound = int(input())
n = 1
maximum = 0
while  0 < n <= bound:
    if n % divisor == 0:
        if n > maximum:
            maximum = n
    n += 1

print(maximum)

"""
# second way
divisor = int(input())
bound = int(input())
for num in range(bound,0,-1):
    if num % divisor == 0:
        print(num)
        break
"""