steps = 0

extra = 0
while steps < 10000:
    command = input()
    if command == "Going home":
        extra = int(input())
        steps += extra
        break
    steps += int(command)
if steps >= 10000:
    print("Goal reached! Good job!")
else:
    print(f"{10000-steps} more steps to reach goal.")