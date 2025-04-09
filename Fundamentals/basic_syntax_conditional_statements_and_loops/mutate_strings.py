str_one = input()
str_two = input()
for i in range(len(str_one)):  # Loop over each character in str_one.
    if str_one[i] != str_two[i]:  # Check if characters at index i are different in both strings.
        for str_two_index in range(0, i + 1):  # Loop through characters of str_two up to index i.
            print(str_two[str_two_index], end="")  # Print characters from str_two up to index i, without a newline.

        for str_one_index in range(i + 1,len(str_one)):  # Loop through the remaining characters in str_one after index i.
            print(str_one[str_one_index], end="")  # Print the remaining characters from str_one.

        print()  # Print a newline after completing this iteration.
