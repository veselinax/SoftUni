args = input().split()
first_word = args[0]
second_word = args[1]

min_len = min(len(first_word), len(second_word))   # Find the length of the shorter word
total_sum = 0

# Multiply character codes of matching positions and add to the total
for i in range(min_len):
    total_sum += ord(first_word[i]) * ord(second_word[i])

# Determine which word is longer to handle extra characters
long_word = ""
if len(first_word) > len(second_word):
    long_word = first_word
else:
    long_word = second_word

# Add the ASCII values of the remaining characters in the longer word
for index in range(min_len, len(long_word)):
    total_sum += ord(long_word[index])
print(total_sum)