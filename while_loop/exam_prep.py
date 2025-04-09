bad_grades__max_count = int(input())

bad_grades = 0
sum_grades = 0
total_grades = 0
last_problem = ''
failed = True

while bad_grades < bad_grades__max_count:
    text = input()
    if text == "Enough":
        failed = False
        break
    grade = int(input())
    if grade <= 4:
        bad_grades +=1
    sum_grades += grade
    total_grades += 1
    last_problem = text
if failed:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {(sum_grades/total_grades):.2f}")
    print(f"Number of problems: {total_grades}")
    print(f"Last problem: {last_problem}")

