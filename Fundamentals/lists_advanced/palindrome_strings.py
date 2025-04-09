words = input().split()
searched_palindrome = input()
palindrome = []

for word in words:
    if word == "".join(reversed(word)):  # checking if the word is palindrome
        palindrome.append(word)  # adding it to the list of palindromes
pal_count = palindrome.count(searched_palindrome)  # how many times we have it
print(f"{palindrome}")
print(f"Found palindrome {pal_count} times")