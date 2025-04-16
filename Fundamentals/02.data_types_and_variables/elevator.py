number_of_people = int(input())
capacity = int(input())
courses = 0

if number_of_people < capacity:  # all people can fit in the elevator in one course
    courses = 1
else:
    res = number_of_people // capacity    # without reminder
    courses += res
    if number_of_people % capacity != 0:  # if there is reminder we add one more course
        courses += 1
print(courses)