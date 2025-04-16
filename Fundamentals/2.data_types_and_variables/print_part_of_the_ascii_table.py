start = int(input())
end = int(input())

for i in range(start, end+1):  # end inclusive so we add 1
    print(chr(i),end=" ") # chr prints the symbols from the ascii table and end=" " prints them on same line with space)
# if we dont want space between them we can write end=""