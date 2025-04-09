first_char = input()
last_char = input()

def chars_in_range(start,end):
    res = ""
    for i in range(ord(start) + 1, ord(end)):  # numbers of ascii code so we get the range excluding first and last
        res += chr(i) + " " # transforming to symbols and adding space between them
    return res

print(chars_in_range(first_char,last_char))