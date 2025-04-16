number = float(input())
entry = input()
result = input()
if entry == "mm":
    if result == "cm":
        changed = number / 10  # cm = mm/10
    elif result == "m":
        changed = number / 1000 # m = mm/1000
elif entry == "cm":
    if result == "mm":
        changed = number * 10 # mm = cm * 10
    elif result == "m":
         changed = number / 100 # m = cm/100
elif entry == "m":
    if result == "cm":
        changed = number * 100 # cm = m*100
    elif result == "mm":
        changed = number * 1000 # mm = m*1000

print(f"{changed:.3f}")


