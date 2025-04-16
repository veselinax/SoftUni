s = int(input())
d = int(input())

cake_size = s * d
taken_pieces = 0


while taken_pieces < cake_size:
    command = input()

    if command == "STOP":
        print(f"{cake_size - taken_pieces} pieces are left.")
        break

    piece = int(command)
    taken_pieces += piece

if taken_pieces >= cake_size:
    print(f"No more cake left! You need {taken_pieces - cake_size} pieces more.")