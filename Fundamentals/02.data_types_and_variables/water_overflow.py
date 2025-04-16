capacity = 255
n = int(input())
pouring = 0

for i in range(n):
    liters = int(input())
    pouring += liters
    if pouring > capacity:
        pouring -= liters
        print("Insufficient capacity!")
print(pouring)

