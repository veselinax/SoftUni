force_sides = {}
user_side = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        side, user = command.split(" | ")

        # Only add if user doesn't exist
        if user not in user_side:
            if side not in force_sides:
                force_sides[side] = []
            force_sides[side].append(user)
            user_side[user] = side

    elif " -> " in command:
        user, side = command.split(" -> ")

        # If user already exists, remove from old side
        if user in user_side:
            old_side = user_side[user]
            force_sides[old_side].remove(user)

        # Add to new side
        if side not in force_sides:
            force_sides[side] = []
        force_sides[side].append(user)
        user_side[user] = side
        print(f"{user} joins the {side} side!")

# Print the final result
for side, users in force_sides.items():
    if users:  # Only print sides with members
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
