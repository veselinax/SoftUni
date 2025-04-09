cards = input().split()  # Split the input into individual cards
team_a = [1] * 11  # List of 11 ones for Team A (all players present initially)
team_b = [1] * 11  # List of 11 ones for Team B (all players present initially)

for card in cards:
    tokens = card.split("-")
    team = tokens[0]  # Team identifier ("A" or "B")
    player = int(tokens[1]) - 1  # Player number (adjusted for 0-based indexing) (task description index - 1)

    if team == "A":
        if team_a[player] == 1:  # If player is still on the field (not sent off)
            team_a[player] = 0  # Send off the player (set their value to 0)
    else:
        if team_b[player] == 1:  # If player is still on the field (not sent off)
            team_b[player] = 0  # Send off the player (set their value to 0)

    # After each card, check if the game should be terminated (if either team has less than 7 players)
    if sum(team_a) < 7 or sum(team_b) < 7:
        print(f"Team A - {sum(team_a)}; Team B - {sum(team_b)}")
        print("Game was terminated")
        break  # Exit the loop since the game is terminated

else:
    # If the loop finishes without termination, print the remaining players
    print(f"Team A - {sum(team_a)}; Team B - {sum(team_b)}")
