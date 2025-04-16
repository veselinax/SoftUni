payments_count = int(input())

paying = 0
balance = 0

while paying < payments_count:
    amount_to_pay = float(input())

    if amount_to_pay < 0:
        print("Invalid operation!")
        break                           # the while loop stops

    print(f"Increase: {amount_to_pay:.2f}")
    paying += 1
    balance += amount_to_pay
print(f"Total: {balance:.2f}")
