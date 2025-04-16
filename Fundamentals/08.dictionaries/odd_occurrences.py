words = input().split()
dictionary = {}

for word in  words:
    word_lower = word.lower()  # check for each word (lower case) if it is in the dictionary, and if it is not, add it
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1
for key, value in dictionary.items(): # create another loop using the items() method
    if value % 2 != 0:  #  check if the occurrence of the current word is odd
        print(key, end=" ")