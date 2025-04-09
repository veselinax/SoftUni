flowers_type = input()
flowers_count = int(input())
budget = int(input())
price = 0  # initializing the variables
discount = 0

if flowers_type == "Roses":
    price = 5
    if flowers_count > 80:
        price -= price * 0.10   # повече от 80 Рози - 10% отстъпка от крайната цена
elif flowers_type == "Dahlias":
    price = 3.80
    if flowers_count > 90:
        price -= price * 0.15
elif flowers_type == "Tulips":
    price = 2.80
    if flowers_count > 80:
        price -= price * 0.15
elif flowers_type == "Narcissus":
    price = 3
    if flowers_count < 120:
        price += price * 0.15  # по-малко от 120 Нарциса - цената се оскъпява с 15%
elif flowers_type == "Gladiolus":
    price = 2.50
    if flowers_count < 80:
        price += price * 0.20
cost = price * flowers_count
if cost <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {(budget-cost):.2f} leva left.")
else:
    print(f"Not enough money, you need {(cost-budget):.2f} leva more.")


