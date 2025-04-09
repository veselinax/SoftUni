n = int(input())  # Read number of lines
opening_count = 0  # Count of opening brackets
closing_count = 0  # Count of closing brackets
previous_command = ""  # Track the previous character

for i in range(n):
    command = input()

    # If it's not a bracket, ignore this line
    if command not in ["(", ")"]:
        continue

    # Check for consecutive opening brackets
    if command == "(" and previous_command == "(":
        print("UNBALANCED")
        break

    # Check for consecutive closing brackets
    if command == ")" and previous_command == ")":
        print("UNBALANCED")
        break

    # Check if a closing bracket appears without a corresponding opening bracket
    if command == ")" and opening_count == 0:
        print("UNBALANCED")
        break

    # Update opening and closing counts based on the current command
    if command == "(":
        opening_count += 1
    elif command == ")":
        closing_count += 1

    previous_command = command

else:  # This else corresponds to the for loop (only executes if the loop completes without a break)
    if opening_count == closing_count:
        print("BALANCED")
    else:
        print("UNBALANCED")
