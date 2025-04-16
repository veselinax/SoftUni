n = int(input())
dictionary = {}

for i in range(n):
    student = input()
    grades = float(input())
    if student not in dictionary:
        dictionary[student] = []
    dictionary[student].append(grades)
for student,grades in dictionary.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")