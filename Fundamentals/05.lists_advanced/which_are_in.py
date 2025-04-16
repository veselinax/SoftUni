list_one = input().split(", ")
list_two = input().split(", ")
substrings = []

for i in list_one:
    for j in list_two:
        if i in j:
            substrings.append(i)
            break  #  # Once we find a match, no need to check further for this string
            #break out of the inner loop to avoid adding the same string multiple times

print(substrings)