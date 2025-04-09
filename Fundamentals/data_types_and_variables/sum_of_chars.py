n = int(input())
total_sum = 0

for i in range(n):
    char = input()
    total_sum += ord(char)  # ord sums the ASCII codes of the characters
print(f"The sum equals: {total_sum}")