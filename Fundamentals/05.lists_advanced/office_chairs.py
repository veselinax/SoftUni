number_of_rooms = int(input())
free_chairs = 0   # we count total at the end so we initialize before the loop
is_over = False

for i in range(1,number_of_rooms+1):
    needed_chairs = 0   # we count needed chair for current room and we refresh back to 0 for every iteration\
    # in the loop thats why it is initialized inside of the loop
    command = input().split()
    x = command[0]
    chairs = len(x)   # number of chairs XXXXX
    visitors = int(command[1])
    if chairs >= visitors:
        free_chairs += chairs - visitors
    else:
        needed_chairs = visitors - chairs
        is_over = True
        print(f"{needed_chairs} more chairs needed in room {i}")
if not is_over:
    print(f"Game On, {free_chairs} free chairs left")


