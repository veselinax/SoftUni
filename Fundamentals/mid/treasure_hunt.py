treasure_chest = input().split("|")
command = input()
sum_length = 0

while command != "Yohoho!":
    action = command.split()
    if action[0] == "Loot":
        items = action[1:]   # takes all items after Loot
        for item in items:
            if item in treasure_chest:
                continue     # skips
            else:
                treasure_chest.insert(0,item)  # inserting at the end of the list
    elif action[0] == "Drop":
        index = int(action[1])
        if index in range(len(treasure_chest)):
            treasure_chest.append(treasure_chest[index])  # first appending the item in the back
            treasure_chest.remove(treasure_chest[index])  # then removing it from the treasure chest list
    elif action[0] == "Steal":
        count = int(action[1])
        stolen = treasure_chest[-count:]  # Get last n items
        treasure_chest = treasure_chest[:-count]  # Remove them from the treasure chest list
        print(f"{', '.join(stolen)}")
    command = input()

if command == "Yohoho!":
    if len(treasure_chest) == 0:
        print("Failed treasure hunt.")
    else:
        for treasure in treasure_chest:
            length = len(treasure)    # gets the length of every treasure in the treasure chest list
            sum_length += length      # sums all lengths
        average = sum_length / len(treasure_chest)   
        print(f"Average treasure gain: {average:.2f} pirate credits.")



