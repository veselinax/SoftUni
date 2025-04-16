# Read input from the user, split by commas, and remove extra spaces
tickets = [ticket.strip() for ticket in input().split(',')]

# The valid winning symbols
winning_symbols = ['@', '#', '$', '^']

# This function finds the longest sequence of a given symbol in a string half
def longest_sequence(half, symbol):
    count = 0          # Current sequence length
    max_count = 0      # Longest sequence found

    for char in half:
        if char == symbol:
            count += 1
            max_count = max(max_count, count)  # Update max if current is longer
        else:
            count = 0  # Reset count when the character changes

    return max_count  # Return the longest sequence found

# Loop through each ticket to check if it's a winner
for ticket in tickets:
    # Step 1: Check if the ticket is exactly 20 characters
    if len(ticket) != 20:
        print("invalid ticket")
        continue  # Skip to the next ticket

    # Step 2: Split the ticket into two halves
    left = ticket[:10]
    right = ticket[10:]

    match_found = False  # Flag to track if a winning match is found

    # Step 3: Check each valid symbol to see if there's a winning sequence
    for symbol in winning_symbols:
        left_count = longest_sequence(left, symbol)     # Longest sequence in left half
        right_count = longest_sequence(right, symbol)   # Longest sequence in right half

        match_length = min(left_count, right_count)     # Match length is the smaller of the two

        if match_length >= 6:  # A valid winning match
            if match_length == 10:
                # Jackpot condition (10 repeating symbols on both sides)
                print(f'ticket "{ticket}" - {match_length}{symbol} Jackpot!')
            else:
                # Regular match (6 to 9)
                print(f'ticket "{ticket}" - {match_length}{symbol}')
            match_found = True
            break  # No need to check other symbols once a match is found

    # Step 4: If no symbol matched, print "no match"
    if not match_found:
        print(f'ticket "{ticket}" - no match')
