string_input = input()

def odd_even_sum(string):
    even_sum = 0
    odd_sum = 0

    for i in string:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        if i % 2 != 0:
            odd_sum += i
    res = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return res

print(odd_even_sum(string_input))