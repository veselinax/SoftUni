cypher = input().split()  # Read a string input, split by spaces to get a list of words (ciphered text)
answer = []  # Initialize an empty list to store the decoded words

for i in cypher:  # Loop through each word in the cypher list
    result = chr(
        int(''.join(list(filter(str.isdigit, i)))))  # Extract digits, convert to an integer, then to a character
    reminder = ''.join(list(filter(str.isalpha, i)))  # Extract all alphabetic characters from the word

    # Check if the alphabetic characters are a single character or more
    if len(reminder) <= 1:
        result += reminder  # If it's a single character, append it directly to the result
        answer.append(result)  # Add the resulting word to the answer list
    else:
        # Rearrange the alphabetic characters: move the last character to the front
        reminder = reminder[-1] + reminder[1:-1] + reminder[0]
        result += reminder  # Append the rearranged characters to the result
        answer.append(result)  # Add the resulting word to the answer list

# Join the answer list into a string and print the result
print(' '.join(answer))
