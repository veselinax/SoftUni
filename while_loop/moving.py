s = int(input())
d = int(input())
v = int(input())

done = False
taken_space = 0
free_space = s * d * v

while taken_space < free_space:
    command = input()

    if command == "Done":
        done = True
        break
    taken_space += int(command)            # if it's not Done the commands are numbers so we transfer the string to int
if done:
    print(f"{(free_space - taken_space)} Cubic meters left.")
else:
    print(f"No more free space! You need {(taken_space - free_space)} Cubic meters more.")
