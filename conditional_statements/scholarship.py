import math

income = float(input())
average_grade = float(input())
minimal_salary = float(input())
if income <= minimal_salary and 4.5 <= average_grade < 5.50:
    scholarship = minimal_salary * 0.35
    print(f"You get a Social scholarship {math.floor(scholarship)} BGN")
elif average_grade >= 5.50 and income > minimal_salary:
    scholarship = average_grade * 25
    print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
elif income <= minimal_salary and average_grade >= 5.50:
    scholarship_min = minimal_salary * 0.35
    scholarship_grade = average_grade * 25
    if scholarship_min > scholarship_grade:
        scholarship = scholarship_min
        print(f"You get a Social scholarship {math.floor(scholarship)} BGN")
    else:
        scholarship = scholarship_grade
        print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
else:
    print("You cannot get a scholarship!")