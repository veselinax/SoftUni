pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health = int(input())
command = input()
stalemate = True

while command != "Retire":
    action = command.split()
    if action[0] == "Fire":
        index = int(action[1])
        damage = int(action[2])
        if index in range(len(warship_status)):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif action[0] == "Defend":
        start_index = int(action[1])
        end_index = int(action[2])
        damage = int(action[3])
        if start_index in range(len(pirate_ship_status)) and end_index in range(len(pirate_ship_status)):
            for i in range(start_index,end_index+1):
                pirate_ship_status[i] -= damage
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
    elif action[0] == "Repair":
        index = int(action[1])
        health = int(action[2])
        if index in range(len(pirate_ship_status)):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health:
                pirate_ship_status[index] = max_health   # cannot exceed max_health so if it's more we put it as max
    elif action[0] == "Status":
        needed_repair = []
        for section in pirate_ship_status:
            if section < max_health * 0.20:
                needed_repair.append(section)
        print(f"{len(needed_repair)} sections need repair.")
    command = input()

if command == "Retire" and stalemate:
    print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")