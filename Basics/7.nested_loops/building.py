rows = int(input())  # floors
columns = int(input())  # rooms
for floor in range(rows, 0, -1):  # for-цикъл, който итерира броя на етажите от сградата в низходящ ред
    for room in range(0, columns):  # вложен for-цикъл, който да итерира броя на стаите за всеки етаж
        if floor == rows:         # top floor
            print(f"L{floor}{room}" , end=' ')  #The end=' ' argument prevents the default newline character and instead prints
                                                # a space after each room's label, which makes the rooms appear on the same line
        elif floor % 2 == 0:
            print(f"O{floor}{room}" , end=' ')
        else:
            print(f"A{floor}{room}" , end=' ')
    print()     # This ensures a new line after printing all rooms for the current floor.
#After the inner for loop finishes iterating through all rooms on a given floor, \
# the print() function with no arguments is called, which moves the output to a new line \
# before the next floor starts being printed.
