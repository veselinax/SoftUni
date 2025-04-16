# Read the input string from the user
text = input()

# These will hold temporary and final results
current_string = ""  # To collect non-digit characters (part to be repeated)
number = ""          # To collect digits (how many times to repeat current_string)
rage_message = ""    # Final result message

i = 0  # Index for iterating over the input text
while i < len(text):
    # First, collect all non-digit characters into current_string
    while i < len(text) and not text[i].isdigit():
        current_string += text[i]
        i += 1

    # Now collect all digits (could be more than one digit like "12")
    while i < len(text) and text[i].isdigit():
        number += text[i]
        i += 1

    # If we have a number (not an empty string), we process the pair
    if number:
        repeat = int(number)  # Convert the string number to an integer
        # Repeat the current_string (converted to uppercase) 'repeat' times
        rage_message += current_string.upper() * repeat
        # Reset the temporary variables for the next sequence
        current_string = ""
        number = ""

# Use a set to count unique characters in the final message
unique_symbols = set(rage_message)

# Print the number of unique symbols
print(f"Unique symbols used: {len(unique_symbols)}")
# Print the full rage message
print(rage_message)
