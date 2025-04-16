interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
found = False
combinations = 0

for i in range(interval_start, interval_end+1):
    for j in range(interval_start, interval_end+1):
        combinations += 1
        if i + j == magic_number:
            print(f"Combination N:{combinations} ({i} + {j} = {magic_number})")
            found = True
            break
    if found:
        break           # so it stops looking for other combinations and get the first occurrence
if not found:
    print(f"{combinations} combinations - neither equals {magic_number}")