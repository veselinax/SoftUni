import math

L = float(input())
W = float(input())
A = float(input())

area_room = L * W
skameika = area_room / 10  # 10 times smaller means divided by 10
wardrobe_area = A * A
dancer_space = 7040 / 10000 # res = 0.704 (res/10000 cm^2 -> meters)
free_space = area_room - skameika - wardrobe_area
dancers_count = free_space // dancer_space
print(math.floor(dancers_count))