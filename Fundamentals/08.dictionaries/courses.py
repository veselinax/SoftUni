dictionary = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break
    course_name = command[0]
    registered_students = command[1]
    if course_name not in dictionary:
        dictionary[course_name] = []  # list because students can be more than 1
    dictionary[course_name].append(registered_students)
for course,students in dictionary.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")

