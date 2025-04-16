def tribonacci(num):
    # Starting list with the first three numbers of the Tribonacci sequence
    seq = [1, 1, 2]

    # Generate the sequence up to the 'num' numbers
    for i in range(3, num):  #  For each number from the 4th term to the num-th term, we append the sum of the last three numbers in the sequence
        seq.append(seq[-1] + seq[-2] + seq[-3])

    # Print the numbers in the sequence
    for number in seq[:num]:  # from the start till the given number
        print(number, end=" ")  # printing on same line with a space


# Input: Read the number of terms
num = int(input())

# Call the function to print the Tribonacci sequence
tribonacci(num)
