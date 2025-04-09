string_input = input().split()

def abs_values(string):
    int_list = [abs(float(i)) for i in string_input]
    return int_list

print(abs_values(string_input))