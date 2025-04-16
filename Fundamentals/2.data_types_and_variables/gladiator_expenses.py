lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

armor_repair = 0
helmet_repair = 0
sword_repair = 0
shield_repairs = 0

for i in range(1,lost_fights_count+1):
    if i % 2 == 0 and i % 3 == 0: # Shield repair happens when both helmet and sword need repair (i.e., when i is divisible by both 2 and 3)
        shield_repairs += 1
        if shield_repairs % 2 == 0:  #Every time shield repairs happen, armor needs repair too (every 2nd shield repair)
            armor_repair += 1
    if i % 2 == 0:
        helmet_repair += 1
    if i % 3 == 0:
        sword_repair += 1
expenses = sword_price * sword_repair + helmet_price * helmet_repair + shield_price * shield_repairs + armor_price * armor_repair
print(f"Gladiator expenses: {expenses:.2f} aureus")
