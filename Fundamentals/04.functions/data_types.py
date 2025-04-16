input_type = input()
command = input()

def data_types(type_data,n):
    res = None
    if type_data == "int":
        n = int(n)
        res = n * 2
    elif type_data == "real":
        n = float(n)
        res = f"{(n * 1.5):.2f}"
    elif type_data == "string":
        res = "$" + n + "$"
    return res


print(data_types(input_type,command))
