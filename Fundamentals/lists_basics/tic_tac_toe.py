#mistake
# Input the field as three lines of space-separated numbers
field = [list(map(int, input().split())) for _ in range(3)]

# Check rows
for row in field:
    if row[0] == row[1] == row[2]:
        if row[0] == 1:
            print("First player won")
            break
        elif row[0] == 2:
            print("Second player won")
            break
else:
    # Check columns
    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col]:
            if field[0][col] == 1:
                print("First player won")
                break
            elif field[0][col] == 2:
                print("Second player won")
                break
    else:
        # Check diagonals
        if field[0][0] == field[1][1] == field[2][2]:
            if field[0][0] == 1:
                print("First player won")
            elif field[0][0] == 2:
                print("Second player won")
        elif field[0][2] == field[1][1] == field[2][0]:
            if field[0][2] == 1:
                print("First player won")
            elif field[0][2] == 2:
                print("Second player won")
        else:
            print("Draw!")
