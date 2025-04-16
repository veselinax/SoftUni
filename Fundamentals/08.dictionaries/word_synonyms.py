n = int(input())
dictionary = {}

for i in range(n):
    word = input()
    synonym = input()
    #We check if the word is not in the dictionary and in that case we set its value to an empty list\
    # (since one word can have multiple synonyms) and we append the new synonym to that list
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)
for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")


