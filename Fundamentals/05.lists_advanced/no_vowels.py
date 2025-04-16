text = input()
my_string = [x for x in text if x not in ['a', 'o', 'u', 'e', 'i','A','O','U','E','I']]
print("".join(my_string)) # joining all into a string without space