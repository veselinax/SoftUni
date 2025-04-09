operator_input = input()
first_num = int(input())
second_num = int(input())

def solve(operator, i, j):
    res = None
    if operator == "multiply":
        res =  i * j
    elif operator == "divide":
        res = i // j
    elif operator == "subtract":
        res =  i - j
    elif operator == "add":
        res =  i + j
    return res
print(solve(operator_input,first_num,second_num))