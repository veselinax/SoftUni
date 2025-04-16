def get_alphabet_position(letter):
    return ord(letter.lower()) - 96

strings = input().split()
total_sum = 0

for item in strings:
    first_letter = item[0]
    last_letter = item[-1]
    number = int(item[1:-1])  # Extract the number between letters (from second till end(not included))

    # Apply operation based on the first letter
    if first_letter.isupper():
        number /= get_alphabet_position(first_letter)
    else:
        number *= get_alphabet_position(first_letter)

    # Apply operation based on the last letter
    if last_letter.isupper():
        number -= get_alphabet_position(last_letter)
    else:
        number += get_alphabet_position(last_letter)

    total_sum += number

# Print result rounded to 2 decimal places
print(f"{total_sum:.2f}")
