budget = float(input())
statists_count = int(input())
clothes_expenses_for_one_statist = float(input())
decor = budget * 0.10  # 10% of the budget
if statists_count > 150:
     clothes_expenses_for_one_statist -= clothes_expenses_for_one_statist * 0.10  # discount = price - (price * 0.10) -> 10% discount
expenses =  (clothes_expenses_for_one_statist*statists_count) + decor
if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {(expenses-budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget - expenses):.2f} leva left.")