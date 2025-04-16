allowed_quantity = int(input())
days_till_christmas = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
spirit = 0
bought = 0
for i in range(1,days_till_christmas+1):
    if i % 11 == 0:
        allowed_quantity += 2     # this first cuz it changes the quantity for everything down if reached
    if i % 2 == 0:
        bought += ornament_set * allowed_quantity
        spirit += 5
    if i % 3 == 0:
        bought += tree_skirt * allowed_quantity
        bought += tree_garlands * allowed_quantity
        spirit += 13
    if i % 5 == 0:
        bought += tree_lights * allowed_quantity
        spirit +=17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        bought += tree_skirt + tree_garlands + tree_lights
        if i == 10 and days_till_christmas % 10 == 0:  # if 10 is the last day
            spirit -= 30

print(f"Total cost: {bought}")
print(f"Total spirit: {spirit}")


