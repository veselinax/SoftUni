name = input()
year = 1
grades_sum = 0
while year <= 12:
    grade = float(input())
    if grade >= 4.00:
        year += 1
        grades_sum += grade
print(f"{name} graduated. Average grade: {(grades_sum/12):.2f}")