password = input()


def password_check(password):
    # Check if the length is between 6 and 10 characters
    condition_1 = 6 <= len(password) <= 10

    # Check if the password consists only of letters and digits
    condition_2 = password.isalnum()

    # Check if the password has at least 2 digits
    digit_count = sum(1 for char in password if char.isdigit())
    condition_3 = digit_count >= 2

    # Print messages for each failed condition
    if not condition_1:
        print("Password must be between 6 and 10 characters")
    if not condition_2:
        print("Password must consist only of letters and digits")
    if not condition_3:
        print("Password must have at least 2 digits")

    # If all conditions are met, print "Password is valid"
    if condition_1 and condition_2 and condition_3:
        print("Password is valid")



password_check(password)
