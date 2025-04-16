year = int(input())
while True:
    year += 1 # We increment the year first because we want the next year after the input year
    distinct_digits = set(str(year))  #We convert the year into a string and then into a set to get unique digits
    #This checks if the number of digits (length of the string) is equal to the number of distinct digits\
    # (length of the set). If this is true, the year has distinct digits
    if len(str(year)) == len(distinct_digits):
        break  #We exit the loop when the next year with distinct digits is found
print(year)