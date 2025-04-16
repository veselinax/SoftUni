n = int(input())
combinations = 0

#3 вложени for цикъла, с които да итерираме всяка възможна стойност на едно от 3-те числа в уравнението x1 + x2 + x3 = n
for i in range(0, n+1):
    for j in range(0,n+1):
        for k in range(0,n+1):
            if i + j + k == n:
                combinations += 1

print(combinations)