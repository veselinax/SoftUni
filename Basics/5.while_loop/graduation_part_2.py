name = input()

year = 1
grades_sum = 0
repeat = 0
excluded = False

while year <= 12:
    grade = float(input())

    if grade >= 4.00:
        year += 1
        grades_sum += grade
    else:
        repeat += 1
    if repeat == 2:
        excluded = True
        break             # we stop the loop

if excluded:              # if True
    print(f"{name} has been excluded at {year} grade")
else:
    print(f"{name} graduated. Average grade: {(grades_sum/12):.2f}")