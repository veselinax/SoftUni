open_tabs = int(input())
salary = int(input())
no_salary = False

for i in range(open_tabs):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
    if salary == 0:
        no_salary = True
        break
if no_salary:
    print("You have lost your salary.")
else:
    print(round(salary))