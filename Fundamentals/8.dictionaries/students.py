students = {}

while True:
    line = input()
    if ":" not in line:
        course_to_find = line.replace("_", " ")
        break

    name, student_id, course = line.split(":")
    students[name] = student_id, course

for name, (student_id, course) in students.items():
    if course == course_to_find:
        print(f"{name} - {student_id}")