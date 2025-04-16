n = int(input())  # Read n
l = int(input())  # Read l

# Create a list of possible passwords
passwords = []

for digit1 in range(1, n + 1):
    for digit2 in range(1, n + 1):
        for letter1 in range(l):
            for letter2 in range(l):
                for digit3 in range(1, n + 1):
                    # Check that digit3 is greater than both digit1 and digit2
                    if digit3 > max(digit1, digit2):
                        password = f"{digit1}{digit2}{chr(97 + letter1)}{chr(97 + letter2)}{digit3}"   #For the letters, we generate the first l letters of the alphabet using chr(97 + index) to get 'a', 'b', etc.
                        passwords.append(password)

# Print all passwords in alphabetical order
print(" ".join(sorted(passwords)))
