n = int(input())

# We create the first loop, which will print half of the pattern until i == number:
# We create the inner loop through the numbers from 0 to i (i is not inclusive). We use end='' \
# to stay on the same line. We print the new line after we draw all the stars for the particular line.
for i in range(1, n + 1):  # rows
    for j in range(0, i):  # columns
        print("*", end="")
    print()
# Next, we create the second loop backward as we \
# need to decrease the number of stars with each line. It should draw one line less than the previous one
for i in range(n - 1, 0, -1):  # rows
    for j in range(0, i):  # columns
        print("*", end="")
    print()
