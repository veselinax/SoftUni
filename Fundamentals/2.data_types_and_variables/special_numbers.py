n = int(input())

for i in range(1,n+1):
    digits_sum = 0
    for digit in str(i):
        digits_sum += int(digit)
    is_special = digits_sum == 5 or digits_sum == 7 or digits_sum == 11
    print(f"{i} -> {is_special}")