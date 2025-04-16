string_input = input().split()

def rounding(string):
    numbers_float = [float(x) for x in string]
    numbers_rounded = [round(x) for x in numbers_float]
    return numbers_rounded

print(rounding(string_input))
