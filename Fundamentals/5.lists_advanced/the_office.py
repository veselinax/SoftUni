employee_happiness = input().split()
happiness_improvement = int(input())
sum_happiness = 0

num_employee_happiness = list(map(lambda x: int(x) * happiness_improvement,employee_happiness))  # making the numbers int and multiplying with the improvement number
for i in num_employee_happiness:
    sum_happiness += i     # counting the sum of all
average = sum_happiness / len(num_employee_happiness) # counting average
filtered_employee_happiness = list(filter((lambda x: x >= average),num_employee_happiness))  # filtering those who are >= than the average
happy_count = len(filtered_employee_happiness)  # count of filtered
total_count = len(num_employee_happiness)   # count of all
if happy_count >= total_count/ 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
