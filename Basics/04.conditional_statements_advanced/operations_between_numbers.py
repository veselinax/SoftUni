n1 = int(input())
n2 = int(input())
operator = input()

if operator == "+":
    res = n1 + n2
    if res % 2 == 0:
        test = "even"
    else:
        test = "odd"
    print(f"{n1} + {n2} = {res} - {test}")
if operator == "-":
    res = n1 - n2
    if res % 2 == 0:
        test = "even"
    else:
        test = "odd"
    print(f"{n1} - {n2} = {res} - {test}")
if operator == "*":
    res = n1 * n2
    if res % 2 == 0:
        test = "even"
    else:
        test = "odd"
    print(f"{n1} * {n2} = {res} - {test}")
if operator == "/" and not n2 == 0:
    res = n1 / n2
    print(f"{n1} / {n2} = {res:.2f}")
if operator == "/" and n2 == 0:
    print(f"Cannot divide {n1} by zero")
if operator == "%" and not n2 == 0:
    res = n1 % n2
    print(f"{n1} % {n2} = {res}")
if operator == "%" and n2 == 0:
    print(f"Cannot divide {n1} by zero")