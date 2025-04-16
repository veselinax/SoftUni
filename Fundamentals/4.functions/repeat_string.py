string_input = input()
counter = int(input())

repeat_str = lambda a, b: a * b  # small one-time anonymous function
print(repeat_str(string_input,counter))
