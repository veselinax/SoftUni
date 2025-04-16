usernames = input().split(", ")

valid_usernames = []

for username in usernames:
    # Check if the username is between 3 and 16 characters
    # and contains only letters, digits, hyphens (-), or underscores (_)
    # char.isalnum checks if the character is a letter or a digit (no symbols or spaces allowed)
    # all() returns True only if every character passes the condition inside
    if 3 <= len(username) <= 16 and all(char.isalnum() or char in "-_" for char in username):
        valid_usernames.append(username)

for name in valid_usernames:
    print(name)
