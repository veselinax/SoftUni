gifts = input().split()

command = input()
while command != "No Money":
    my_list = command.split()
    gift = my_list[1]          # the second index
    if "OutOfStock" in my_list:
        for i in range(len(gifts)):
            if gifts[i] == gift:  # checking if we have that gift in the gifts list
                gifts[i] = None # replacing with None
    if "Required" in my_list:
        index = int(my_list[2]) # the third index and making it int because it is str
        if index in range(len(gifts)): # ensuring the index is valid
            gifts[index] = gift # replacing the gift with that index with the new gift
    if "JustInCase" in my_list:
        gifts[-1] = gift # replacing the last item of the list with thr new gift
    command = input()
else:
    filtered = [x for x in gifts if x is not None] # removing Nones with comprehension
    print(" ".join(filtered)) # printing as a string separated with spaces