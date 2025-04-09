string_input = input().split(", ")


def is_palindrome(string):
    return string == string[::-1]  # Return True if string is palindrome, else False (string equal to reversed string)

# Loop through the list and check each item
for item in string_input:
    print(is_palindrome(item))   # so we can print for every number true or false on new line
